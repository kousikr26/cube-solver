##import cv2
##import numpy as np
##kernel=np.ones((5,5),np.uint8)
##
##lower_white = np.array([0,0,0], dtype=np.uint8)
##upper_white = np.array([0,0,255], dtype=np.uint8)
##cap=cv2.VideoCapture(0)
##while True:
##    _,frame=cap.read()
##    cv2.imshow('org',frame)
##    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
##    etval2,threshold=cv2.threshold(frame,200,255,cv2.THRESH_BINARY)
##    cv2.imshow('mask',threshold)
##    
##    k=cv2.waitKey(5) & 0xFF
##    if k==ord('q') or k==27:
##        break
##
##cap.release()
##
##cv2.destroyAllWindows()

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)
lower_white = np.array([0,0,0], dtype=np.uint8)
upper_white = np.array([255,15,255], dtype=np.uint8)


while(1):

    _, frame = cap.read()
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    # change it according to your need !


    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(img_hsv, lower_white, upper_white)
    # Bitwise-AND mask and original image
    

    cv2.imshow('frame',frame)
    cv2.imshow('whitemask',mask)








    #red
    lower_red = np.array([0,50,50])#HSV VAUES WILL BE DIFFERENT
    upper_red = np.array([10,255,255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
    #cv2.imshow('mask0',mask0)
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
    #cv2.imshow('mask1',mask1)

    redmask = mask0+mask1

    redmask=cv2.erode(redmask,kernel,iterations=2)#use different iterations and kernels
    redmask=cv2.dilate(redmask,kernel,iterations=2)
    
    cv2.imshow('r',redmask)
    



    #blue
    lower_blue=np.array([80,100,0])#Check blue value doesnt conflict with background
    upper_blue=np.array([140,255,255])
    bluemask=cv2.inRange(img_hsv,lower_blue,upper_blue)#HSV VAUES WILL BE DIFFERENT

    bluemask=cv2.erode(bluemask,kernel,iterations=2)
    bluemask=cv2.dilate(bluemask,kernel,iterations=2)


    cv2.imshow('b',bluemask)

    #green
    lower_green=np.array([41,0,0])#HSV VAUES WILL BE DIFFERENT
    upper_green=np.array([80,255,255])
    greenmask=cv2.inRange(img_hsv,lower_green,upper_green)
    greenmask=cv2.erode(greenmask,kernel,iterations=2)
    greenmask=cv2.dilate(greenmask,kernel,iterations=2)

    cv2.imshow('g',greenmask)

    #yellow
    lower_yellow=np.array([8,39,64])#HSV VAUES WILL BE DIFFERENT
    upper_yellow=np.array([18,255,255])
    yellowmask=cv2.inRange(img_hsv,lower_yellow,upper_yellow)
    yellowmask=cv2.erode(yellowmask,kernel,iterations=2)
    yellowmask=cv2.dilate(yellowmask,kernel,iterations=2)

    cv2.imshow('y',yellowmask)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
