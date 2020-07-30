import cv2
import numpy as np


#cap = cv2.VideoCapture(0)

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')
cv2.resizeWindow('result', 600,600)
# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
cv2.createTrackbar('v', 'result',0,255,nothing)
cv2.createTrackbar('hu', 'result',0,179,nothing)
cv2.createTrackbar('su', 'result',0,255,nothing)
cv2.createTrackbar('vu', 'result',0,255,nothing)




while(1):
    #frame=cv2.imread('yellownoise.jpg',-1)
    #_, frame = cap.read()
    frame=cv2.imread("45.png")
    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    h = cv2.getTrackbarPos('h','result')
    s = cv2.getTrackbarPos('s','result')
    v = cv2.getTrackbarPos('v','result')
    hu = cv2.getTrackbarPos('hu','result')
    su = cv2.getTrackbarPos('su','result')
    vu = cv2.getTrackbarPos('vu','result')

    # Normal masking algorithm
    lower_blue = np.array([h,s,v])
    upper_blue = np.array([hu,su,vu])

    mask = cv2.inRange(hsv,lower_blue, upper_blue)
    cv2.imshow('mask',mask)
    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('resultnew',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

#cap.release()

cv2.destroyAllWindows()
