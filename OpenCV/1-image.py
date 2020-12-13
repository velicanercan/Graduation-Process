# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:58:22 2020

@author: Velican
"""

import cv2
#%%
""" Image """
img = cv2.imread("C:/Users/Velican/Desktop/Graduation Progress/OpenCV/p.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0)

#%%
""" Video """
cap = cv2.VideoCapture("C:/Users/Velican/Desktop/Graduation Progress/OpenCV/try.mp4")

while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
#%%
""" Webcam """
cap = cv2.VideoCapture(0)
cap.set(3,640) #size of weight
cap.set(4,480) #size of height
cap.set(10,100) #brightness
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break