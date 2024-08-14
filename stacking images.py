import cv2
import numpy as np
img = cv2.imread('BB.png')

# resize(col , rows) --> (width , height)
img = cv2.resize(img , (600,500))

hor = np.hstack([img , img])
ver = np.vstack([img , img])

cv2.imshow('horizontal window' , hor)
cv2.imshow('vertical window' , ver)


cv2.imshow('image' , img)
cv2.waitKey(0)