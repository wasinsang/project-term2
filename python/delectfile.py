import cv2
name = "2.jpg"
img = cv2.imread(name)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyWindow('image')
