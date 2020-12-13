# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:42:48 2020

@author: Velican
"""

""" Joining Images : matrislerle çalıştığımız için birleştirilecek fotoğrafların aynı 
                    kanal sayısına sahip olması gerekir.Yani bir foto gray diğeri RGB
                    ise bu method çalışmaz."""
                    
import cv2
import numpy as np

img = cv2.imread("C:/Users/Velican/Desktop/Graduation Progress/OpenCV/p.jpg")

hor = np.hstack((img,img))
ver = np.vstack((img,img))


cv2.imshow("Vertical",ver)
cv2.imshow("Horizontal",hor)





cv2.waitKey(0)