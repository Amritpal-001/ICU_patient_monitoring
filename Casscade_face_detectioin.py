
import imutils
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import cv2
import numpy as np
import os
import time

from utlils_file import *

#black_and_white = False
#webcam = False
#Video_path = None
from input_variables import *

def face_classifier(face_classifier_path):
    face_classifier = cv2.CascadeClassifier(face_classifier_path)
    return(face_classifier)

def eye_classifier(eye_classifier_path):
    eye_classifier = cv2.CascadeClassifier(eye_classifier_path)
    return(eye_classifier)

face_classifier = face_classifier(face_classifier_path)
eye_classifier = eye_classifier(eye_classifier_path)


def frame_extractor(frame , classifier_type ,  black_and_white = False):
    # Function detects faces or any clasifier and returns the cropped face
    if black_and_white == True:
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    extracted_frame = classifier_type.detectMultiScale(frame , 1.3, 5)
    if extracted_frame is ():
        return None
    # Crop all faces found
    for (x, y, w, h) in extracted_frame:
        x = x - 10
        y = y - 10
        cropped_frame = frame[y:y + h + 50, x:x + w + 50]
    return cropped_frame


def frame_Capture_track(classifier_type , Video_path , webcam , black_and_white ):
    # Initialize Webcam
    if webcam == True:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(Video_path)
    count = 0
    starttime = time.time()

    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=500)

        if frame_extractor(frame, classifier_type) is None:
            starttime = time.time()
            #patient_left_logs.append()

        if frame_extractor(frame , classifier_type) is not None:
            count += 1
            extracted_frame = cv2.resize(frame_extractor(frame , classifier_type), (800, 800))
            if black_and_white == True:
                extracted_frame = cv2.cvtColor(extracted_frame, cv2.COLOR_BGR2GRAY)

            # Put count on images and display live count
            font_size = 0.5
            font_color = (0 , 255 , 0)   # Black = (0, 255, 0)
            font_thickness = 1
            x_coordinate = 650
            cv2.putText(extracted_frame, str(time_tracking_function(starttime)), (x_coordinate, 700),
                        cv2.FONT_HERSHEY_COMPLEX, font_size , font_color, font_thickness)
            cv2.putText(extracted_frame, str(current_date_variable()), (x_coordinate, 720),
                        cv2.FONT_HERSHEY_COMPLEX, font_size, font_color, font_thickness)
            cv2.putText(extracted_frame, str(current_time_variable()), (x_coordinate , 740),
                        cv2.FONT_HERSHEY_COMPLEX, font_size, font_color, font_thickness)
            cv2.imshow('Frame cropper', extracted_frame)
    
        else:
            print("Face not found")
            pass
    
        if cv2.waitKey(1) == 13:  # 13 is the Enter Key
            break
    
    cap.release()
    cv2.destroyAllWindows()


frame_Capture_track(face_classifier , input , webcam, black_and_white)

#frame_Capture_track(eye_classifier)


