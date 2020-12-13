# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 00:50:30 2020

@author: Velican
"""

""" Resizing image"""
import cv2

img = cv2.imread(("C:/Users/Velican/Desktop/Graduation Progress/OpenCV/p.jpg"))
print(img.shape)

imgResize = cv2.resize(img,(600,600))
""" Cropping image"""
imgCropped = imgResize[100:500,100:600]

cv2.imshow("Image",img)
cv2.imshow("Image Res",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)