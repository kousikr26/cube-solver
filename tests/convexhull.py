# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 15:55:37 2019

@author: Abdul Ahad
"""

import cv2
def drawlines(img, points):
    filler = cv2.convexHull(points)
    cv2.polylines(img, filler, True, (0, 0, 255),3)
    return img 
#cap=cv2.VideoCapture(0)
#while True:
img=cv2.imread("cube4.jpg")


edges = cv2.Canny(img, 80, 255)


img2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

image = 0

for cnt in contours:
    hull = cv2.convexHull(cnt)
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) #Removes tiny deviations, tries to go for straight lines.
    if len(approx) == 4:
        hull = cv2.convexHull(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 100:
            drawlines(img,cnt)
            print("Width and height: ", w, h)
            """cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
            image = img[y:y+h,x:x+w]"""
            
            
#cv2.rectangle(img,(224,18),(264,56),(100,1,100),3)
cv2.imshow('image', img)
#print(hull)
cv2.imshow('edges', edges)
#cv2.imshow('area', image)
"""if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()"""
cv2.waitKey(0)
cv2.destroyAllWindows()
