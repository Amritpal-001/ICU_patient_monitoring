
import cv2
import os

import time


black_and_white = False
webcam = False

face_classifier_path = 'face_detection_model/haarcascade_frontalface_default.xml'
eye_classifier_path = 'face_detection_model/haarcascade_eye_tree_eyeglasses.xml'
body_classifier_path = 'face_detection_model/haarcascade_fullbody.xml.xml'

face_classifier = cv2.CascadeClassifier(face_classifier_path)
eye_classifier = cv2.CascadeClassifier(eye_classifier_path)


input =  '/home/amritpal/PycharmProjects/100-days-of-code/CEE_final_back/data/single_patient_ICU_1246_movement.mkv'
#print(os.path.basename(input))
prototxt =  'tracking_model/MobileNetSSD_deploy.prototxt'
model =  'tracking_model/MobileNetSSD_deploy.caffemodel'
recognition_model_path = '/home/amritpal/PycharmProjects/100-days-of-code/CEE_final/face_detection_model/trained_model.h5'

output = '/home/amritpal/PycharmProjects/100-days-of-code/CEE_final_back/media/output/' + os.path.basename(input) + str(time.time()) + '.avi'



