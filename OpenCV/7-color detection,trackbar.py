# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:01:29 2020

@author: Velican
"""

""" Color Detection """

import cv2
import numpy as np
def empty(n):
    pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,300)
cv2.createTrackbar("Hue min","TrackBars",33,179,empty)
cv2.createTrackbar("Hue max","TrackBars",66,179,empty)
cv2.createTrackbar("Saturation min","TrackBars",43,255,empty)
cv2.createTrackbar("Saturation max","TrackBars",255,255,empty)
cv2.createTrackbar("Value min","TrackBars",33,255,empty)
cv2.createTrackbar("Value max","TrackBars",255,255,empty)
"""örnek:33 66 43 255 33 255 değerlerini create track bar fonksiyonun içine yazdığımda default olarak 
mask'ı elde ettim.Bu değerleri track bar üzerinde oynayarak buldum."""

while True:
    img = cv2.imread("C:/Users/Velican/Desktop/Graduation Progress/OpenCV/colors.jpg")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue max","TrackBars")
    s_min = cv2.getTrackbarPos("Saturation min","TrackBars")
    s_max = cv2.getTrackbarPos("Saturation max","TrackBars")
    v_min = cv2.getTrackbarPos("Value min","TrackBars")
    v_max = cv2.getTrackbarPos("Value max","TrackBars")
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    imgStack = np.hstack((img,result,imgHSV))
    cv2.imshow("Stack",imgStack)
    # cv2.imshow("Original",img)
    # cv2.imshow("Result",result)
    # cv2.imshow("HSV",imgHSV)
    # cv2.imshow("Mask",mask)
    cv2.waitKey(1)
    