import cv2
import numpy as np

img = cv2.imread("src/sample.png")
print(img.shape)
cv2.imshow("image",img)
imgResize=cv2.resize(img,(300,200))
imgcrop=img[0:200,200:500]
cv2.imshow("imgResize",imgResize)
cv2.imshow("img crop",imgcrop)
cv2.waitKey(0)