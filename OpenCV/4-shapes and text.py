# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 01:10:37 2020

@author: Velican
"""
""" Shapes and Texts """
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# img[:,299:300]=255,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),1)
cv2.rectangle(img,(0,0),(100,100),(0,0,255),cv2.FILLED)
cv2.circle(img,(480,480),30,(255,255,0),cv2.FILLED)
cv2.putText(img," OpenCV ",(272,276),cv2.FONT_HERSHEY_TRIPLEX,1.5,(0,225,0),5)


cv2.imshow("img",img)




cv2.waitKey(0)