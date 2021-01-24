import cv2
import keras
from keras.models import load_model
from PIL import Image
import numpy as np
import os
from glob import glob

from input_variables import *

model = load_model(recognition_model_path)

folderlist = glob('face_detection_model/images/*')
print(folderlist)

for i in range(len(folderlist)):
    name = os.path.basename(folderlist[i])
    print(name)


def face_classifier(face_classifier_path):
    face_classifier = cv2.CascadeClassifier(face_classifier_path)
    return(face_classifier)

face_classifier = face_classifier(face_classifier_path)
video_capture = cv2.VideoCapture(0)  # Doing some Face Recognition with the webcam

def face_extractor(img):
    # Function detects faces and returns the cropped face    # If no face detected, it returns the input image
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    if faces is ():
        return None
    for (x, y, w, h) in faces:  # Crop all faces found
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cropped_face = img[y:y + h, x:x + w]
    return cropped_face


while True:
    _, frame = video_capture.read()
    # canvas = detect(gray, frame)
    # image, face =face_detector(frame)

    face = face_extractor(frame)
    if type(face) is np.ndarray:
        face = cv2.resize(face, (224, 224))
        im = Image.fromarray(face, 'RGB')
        # Resizing into 128x128 because we trained the model with this image size.
        img_array = np.array(im)
        # Our keras model used a 4D tensor, (images x height x width x channel)
        # So changing dimension 128x128x3 into 1x128x128x3
        img_array = np.expand_dims(img_array, axis=0)
        pred = model.predict(img_array)
        pred_class = keras.utils.to_categorical(pred)

        print(pred[0])

        #print(pred[0] , pred_class)
        #print( pred_class)

        name = "None matching"
        Namelist = ['Akshdeep', 'Amrit', 'biswas', 'Kamil', 'Talab', 'Vipul']
        Namelist = ['1' , '2' , '3' , '4', '5' , '6' ]

        for i in range(len(Namelist)):
            if (pred[0][i] > 0.5):
                name = Namelist[i]

        cv2.putText(frame, name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0 ,  0 , 0 ), 2)
    else:
        cv2.putText(frame, "No face found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, ( 0 , 0 , 255), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
