from __future__ import print_function
import cv2 as cv
import argparse
import time

camera = False
from input_variables import *
from utlils_file import *

#input =  '/home/amritpal/PycharmProjects/100-days-of-code/CEE_final/Deep-Learning-Face-Recognition-master/data/koak Box3(1).avi'

parser = argparse.ArgumentParser(description='Face_eye detection - Cascade Classifier')
parser.add_argument('--face_cascade', help='Path to face cascade.', default=face_classifier_path)
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default=eye_classifier_path)
parser.add_argument('--body_cascade', help='Path to eyes cascade.', default=body_classifier_path)
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()

face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
body_cascade_name = args.eyes_cascade
body_cascade = cv.CascadeClassifier()

camera_device = args.camera

#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
if not body_cascade.load(cv.samples.findFile(body_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)


'''def detect_eye_AndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    frame_gray = frame_gray[100:700, 500:800]
    #-- Detect faces
    faces = body_cascade.detectMultiScale(frame_gray)

    #faces = face_extractor(faces)

    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame_gray, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]

        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.1))
            frame = cv.circle(frame_gray, eye_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Face detection', frame_gray)'''


patient_coordinates = 100, 350 , 500, 350
starttime = time.time()

def detect_face_from_cropped_bed(frame ,patient_coordinates):

    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.equalizeHist(frame)
    #frame_gray = frame_gray[100:700, 500:800]
    #frame_gray = frame_gray[x_coordinate:x_coordinate+width, y_coordinate:y_coordinate+height]
    a, b , c , d = patient_coordinates
    e = a + b
    f = c + d
    frame = frame[a:e, c:f]

    faces_detected = face_cascade.detectMultiScale(frame)



    a = 100
    for (x,y,w,h) in faces_detected:
        print(x,y,w,h)
        center = (x + w//2, y + h//2)
        start_point = (x , y)
        end_point = (x+w, y+h)

        #frame_gray = cv.ellipse(frame_gray, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        frame = cv.rectangle(frame, start_point , end_point , (255, 0, 255), int(1) , int(1) )
        faceROI_111 = frame[y-a:y+h+a,x-a:x+w+a]

        # Put count on images and display live count
        font_size = 0.5
        font_color = (0, 255, 0)  # Black = (0, 255, 0)
        font_thickness = 1
        x_coordinate = 170
        y_coordiante = b
        cv2.putText(frame, str(time_tracking_function(starttime)), (x_coordinate, y_coordiante - 70),
                    cv2.FONT_HERSHEY_COMPLEX, font_size, font_color, font_thickness)

        cv2.putText(frame, str(current_date_variable()), (x_coordinate, y_coordiante - 30),
                    cv2.FONT_HERSHEY_COMPLEX, font_size, font_color, font_thickness)
        cv2.putText(frame, str(current_time_variable()), (x_coordinate, y_coordiante - 10),
                    cv2.FONT_HERSHEY_COMPLEX, font_size, font_color, font_thickness)

        cv.imshow('Capture - Face detection', frame)

if camera == True:
    cap = cv.VideoCapture(camera_device)
else:
    cap = cv.VideoCapture(input)

if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    #detect_eye_AndDisplay(frame)
    detect_face_from_cropped_bed(frame , patient_coordinates )
    if cv.waitKey(10) == 27:
        break
