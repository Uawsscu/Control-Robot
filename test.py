import cv2
import numpy as np

img = cv2.imread('/home/uawsscu/PycharmProjects/Project2/data/TrainImg.jpeg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT()
kp = sift.detect(gray,None)
img=cv2.drawKeypoints(gray,kp)
cv2.imwrite('/home/uawsscu/PycharmProjects/Project2/T1.jpg',img)