import cv2
import numpy as np
import os
import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
from imageai.Detection import ObjectDetection
from PIL import Image
import time
import sys
import serial
arduino = serial.Serial('com4', 9600)
execution_path = os.getcwd()
# Playing video from file:
cap = cv2.VideoCapture(0)
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')

currentFrame = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Saves image of the current frame in jpg file
    name = str(currentFrame) + '.jpg'
    print('Creating...' + name)
    cv2.imwrite(name, frame)
    namenew = str(currentFrame + 1) + ".jpg"
    name_detec = str(currentFrame + 2) + ".jpg"
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, namenew),
                                             output_image_path=os.path.join(execution_path, name_detec))
    for eachObject in detections:
        print(eachObject["name"], " : ", eachObject["percentage_probability"])
        var = eachObject["name"]
        if var in "person":
            print("Hello person")
            break
        else:
            print("Nothing")
    image = Image.open(name_detec)
    image.show(image)
    #img = Imageopen(name_detec)
    #cv2.waitKey(0)
    #cv2.imshow('image', img)
    # To stop duplicate images
    currentFrame += 1
    if var in "person":
        print("Hello person")
    else:
        print("Nothing")
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

