#importing libraries
import numpy as np
import tensorflow as tf
from keras_preprocessing.image import img_to_array
import cv2


#load model
model = tf.keras.models.load_model('emotion_detection_model.h5')

face_haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#code for real time detection
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,img=cap.read()
    height, width, channel = img.shape
    sub_img = img[0:int(height/6),0:int(width)]
    heading = np.ones(sub_img.shape, dtype=np.uint8)*0
    result = cv2.addWeighted(sub_img, 0.82, heading,0.18, 0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.9
    font_thickness = 2
    lable = 'Emotion Detection'
    lable_dimension = cv2.getTextSize(lable,font,font_scale,font_thickness)[0]
    textX = int((result.shape[1] - lable_dimension[0]) / 2)
    textY = int((result.shape[0] + lable_dimension[1]) / 2)
    cv2.putText(result, lable, (textX,textY), font, font_scale, (0,0,0), font_thickness)
    lable_color = (255, 255, 0)
    # prediction part 
    gray_image= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect faces on screen
    faces = face_haar_cascade.detectMultiScale(gray_image)
    try:
        for (x,y, w,h) in faces:
            #frame rectangle
            cv2.rectangle(img, pt1 = (x,y),pt2 = (x+w, y+h), color = (255,0,0),thickness = 2)
            roi_gray = gray_image[y-5:y+h+5,x-5:x+w+5]
            roi_gray=cv2.resize(roi_gray,(48,48))
            image_pixels = img_to_array(roi_gray)
            image_pixels = np.expand_dims(image_pixels, axis = 0)
            #normalize
            image_pixels /= 255
            predictions = model.predict(image_pixels)
            max_index = np.argmax(predictions[0])
            #map predictions
            emotion_detection =('Angry', 'Disgusted', 'Fear', "Happy", 'Sad', 'Surprised', 'Neutral')
            emotion_prediction = emotion_detection[max_index]
            cv2.putText(img,emotion_prediction, (int(x+w/3),int(y)),font,0.9, lable_color,2)
            
    except :
        pass
    img[0:int(height/6),0:int(width)] = result
    cv2.imshow('Emotion Detection', img)
    #press Q to close
    if cv2.waitKey(1) == ord('Q'):
        break
#release and destroy video data
cap.release()
cv2.destroyAllWindows()