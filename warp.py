import cv2
import numpy as np
img = cv2.imread("src/sample.png")

width,height = 250,350
pts1= np.float32([[111,219],[287,188],[154,92],[342,448]])
pts2= np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput =cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("image",img)
cv2.imshow("output",imgOutput)
cv2.waitKey(0)