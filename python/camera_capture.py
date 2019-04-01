import cv2

cap = cv2.VideoCapture(0)

currentFrame = 0
while(True):
    ret, frame = cap.read()

    name = str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    currentFrame += 1
cap.release()
cv2.destroyAllWindows()