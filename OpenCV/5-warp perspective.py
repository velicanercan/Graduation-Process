# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:11:22 2020

@author: Velican
"""
""" Warp Perspective : yana doğru eğik bir görüntüyü dikleştirmek"""

import cv2
import numpy as np

width,height= 300,400
img = cv2.imread("C:/Users/Velican/Desktop/Graduation Progress/OpenCV/4aces.png")
# img = cv2.resize(img,(600,600))

pts1 = np.float32([[12,7],[135,7],[12,197],[135,197]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])                 
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOut = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Aces",imgOut)
# cv2.imshow("Aces",img)
cv2.waitKey(0)
