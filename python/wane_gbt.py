from imageai.Detection import ObjectDetection
from PIL import Image
import os
import requests
import cv2

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
im = cv2.imread('imagenew.jpg')
resized_image = cv2.resize(im,(713,392))
cv2.imwrite('img_resize.jpg',resized_image )
token="QYbDmvAbKDy8dmrs9fPmEf0BIye357FYAtl5KYWfRr5"
url = "https://notify-api.line.me/api/notify"

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    var = eachObject["name"]

if var in ('truck'):
    image = Image.open('imagenew.jpg')
    file = {'imageFile': open('img_resize.jpg', 'rb')}
    data = ({'message': 'warning'})
    headers = {"Authorization": "Bearer " + token}
    r = requests.post(url, headers=headers, files=file, data=data)
    print(r.text)
    image.show()
else:
    image = Image.open('imagenew.jpg')
    file = {'imageFile': open('img_resize.jpg', 'rb')}
    data = ({'message': 'No warning'})
    headers = {"Authorization": "Bearer " + token}
    r = requests.post(url, headers=headers, data=data)
    print(r.text)
    image.show()
    print ("Noooooo!!!!!!")
