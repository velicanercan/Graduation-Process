# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 17:36:12 2020

@author: Velican
"""

import cv2
import numpy as np

path = "C:/Users/Velican/Desktop/Graduation Progress/OpenCV/shapes.png"

img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),2)
imgStack = np.stack((imgGray,imgBlur))
imgCanny = cv2.Canny(imgBlur,50,50)
imgContour=img.copy()
def getContours(img):
    contours,hieararchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 130:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x , y , w , h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            
            if objCor==3: ObjectType="Tri"
            elif objCor>7: ObjectType="Circle"
            elif objCor>4: ObjectType="Rectangle"
            else: ObjectType="None"
            cv2.putText(imgContour,ObjectType,(x+(w//2),y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
getContours(imgCanny)
cv2.imshow("Stack",imgContour)

cv2.waitKey(0)