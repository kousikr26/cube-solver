import numpy as np
import cv2

rubik_cascade = cv2.CascadeClassifier('cube.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    
    rubik = rubik_cascade.detectMultiScale(gray, 30, 30)

    for (x,y,w,h) in rubik:
        cv2.rectangle(img,(x,y),(x+2*w,y+2*h),(255,255,0),3)


    cv2.imshow('img',img)
    
    #Release with escape key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
