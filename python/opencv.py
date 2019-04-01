import cv2
cap = cv2.VideoCapture(1)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is True:
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()