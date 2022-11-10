import cv2
import numpy as np

img = cv2.imread("src/sample.png")
kernel=np.ones((5,5),np.uint8)
#imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#median = cv2.medianBlur(img, 5)
#cv2.imshow('Median Blurring', median)
imgcanny=cv2.Canny(img,150,200)
imgdilate=cv2.dilate(imgcanny,kernel,iterations=1)
imgerode=cv2.erode(imgdilate,kernel,iterations=1)
cv2.imshow('canny img',imgcanny)
cv2.imshow('dialtion img',imgdilate)
cv2.imshow('eroded image',imgerode)
#cv2.imshow("gray image",imgGray)

cv2.waitKey(0)