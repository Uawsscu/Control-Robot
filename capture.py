import cv2
cap = cv2.VideoCapture()

while(1):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()