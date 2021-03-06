# Face recognition

# importting the libraries
from PIL import Image
import cv2
from keras.models import load_model
import numpy as np


from keras.preprocessing import image

model=load_model('facefeatures_new_model.h5')

# loading the cascades
face_cascade=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')

def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns th input image
    faces=face_cascade.detectMultiScale(img, 1.3, 5)

    if faces is ():
        return None

    # crop all faces found
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cropped_face=img[y:y+h,x:x+w]
    return cropped_face

# Doing some face Recognition with the webcam
video_capture=cv2.VideoCapture(0)
while True:
    _,frame=video_capture.read()

    face=face_extractor(frame)
    if type(face) is np.ndarray:
        face=cv2.resize(face,(224,224))
        im=Image.fromarray(face,'RGB')
        img_array=np.array(im)
        print("Image dim:",img_array.shape)
        img_array=np.expand_dims(img_array,axis=0)
        print("Expand Image dim:", img_array.shape)
        print(img_array)
        pred=model.predict(img_array)
        print("prediction Image dim:", pred.shape)
        print(pred)

        name="None matching"

        if (pred[0][0]>0.5):
            name='Nitin'
        cv2.putText(frame,name,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    else:
        cv2.putText(frame, "No face found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()