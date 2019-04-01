#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import requests
import urllib.parse
import sys
import cv2

token="QYbDmvAbKDy8dmrs9fPmEf0BIye357FYAtl5KYWfRr5"
url = "https://notify-api.line.me/api/notify"
im = cv2.imread('imagenew.jpg')
resized_image = cv2.resize(im,(713,392))
cv2.imwrite('img_resize.jpg',resized_image )
file = {'imageFile':open('img_resize.jpg','rb')}
data = ({'message':'hihihi'})
headers = {"Authorization":"Bearer "+token}
r=requests.post(url, headers=headers, files=file, data=data)
print(r.text)