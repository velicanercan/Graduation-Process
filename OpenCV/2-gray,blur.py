# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 00:18:55 2020

@author: Velican
"""
import cv2
import numpy as np
img = cv2.imread("C:/Users/Velican/Desktop/Graduation Progress/OpenCV/p.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny= cv2.Canny(img,100,100)
kernel = np.ones((5,5),np.uint8)
imgDialation= cv2.dilate(imgCanny,kernel)

cv2.imshow("imgGray",imgGray)
cv2.imshow("imgBlur",imgBlur)
cv2.imshow("imgCanny",imgCanny)
cv2.imshow("imgDialation",imgDialation)
cv2.waitKey(0)