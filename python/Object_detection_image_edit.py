import os
import cv2
import numpy as np
import tensorflow as tf
import sys
sys.path.append("..")
import requests
from utils import label_map_util
from utils import visualization_utils as vis_util
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
MODEL_NAME = 'inference_graph'
IMAGE_NAME = 'test5.jpg'
token="QYbDmvAbKDy8dmrs9fPmEf0BIye357FYAtl5KYWfRr5"
url = "https://notify-api.line.me/api/notify"
CWD_PATH = os.getcwd()

PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')

PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)

NUM_CLASSES = 3

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

num_detections = detection_graph.get_tensor_by_name('num_detections:0')
image = cv2.imread(PATH_TO_IMAGE)
image_expanded = np.expand_dims(image, axis=0)

(boxes, scores, classes, num) = sess.run(
    [detection_boxes, detection_scores, detection_classes, num_detections],
    feed_dict={image_tensor: image_expanded})

vis_util.visualize_boxes_and_labels_on_image_array(
    image,
    np.squeeze(boxes),
    np.squeeze(classes).astype(np.int32),
    np.squeeze(scores),
    category_index,
    use_normalized_coordinates=True,
    line_thickness=8,
    min_score_thresh=0.80)
threshold = 0.5
objects = []
for index, value in enumerate(classes[0]):
    object_dict = {}
    if scores[0, index] > threshold:
          object_dict[(category_index.get(value)).get('name').encode('utf8')] = \
                        scores[0, index]
          objects.append(object_dict)
print(objects)
im = cv2.imread('image')
resized_image = cv2.resize(image,(640,480))
cv2.imwrite('img_resize.jpg',resized_image )
cv2.imshow('Object detector', image)
cv2.waitKey(0)
b = []
if objects != b:
    file = {'imageFile': open('img_resize.jpg', 'rb')}
    data = ({'message': 'ตรวจพบรถขนาดใหญ่ภายในภาพ'})
    headers = {"Authorization": "Bearer " + token}
    r = requests.post(url, headers=headers, files=file, data=data)
    print(r.text)
else:
    #file = {'imageFile': open('img_resize.jpg', 'rb')}
    #data = ({'message': 'ไม่พบรถขนาดใหญ่ภายในภาพ'})
    #headers = {"Authorization": "Bearer " + token}
    #r = requests.post(url, headers=headers, data=data)
    #print(r.text)
    print ("ไม่พบรถขนาดใหญ่ภายในภาพ")
