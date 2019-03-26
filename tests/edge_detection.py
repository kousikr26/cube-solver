import cv2
import numpy as np
sigma=0.33
cap=cv2.VideoCapture(0)
while True:
    _,img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    v = np.median(gray)

    #---- apply automatic Canny edge detection using the computed median----
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edges = cv2.Canny(gray, 100, 150)
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=2)
    cv2.imshow("edges",edges)
    img2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,contours,-1,(255,0,0),3)
    
    
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) #Removes tiny deviations, tries to go for straight lines.
        
        if len(approx) == 4: #Lines, should be square.
            x, y, w, h = cv2.boundingRect(cnt)
            if w > 10:
                print("Width and height: ", w, h)
                image = img[y:y+h, x:x+w]
                cv2.imshow('area', image)
            

    cv2.imshow('image', img)
    cv2.imshow('edges', edges)
    
    k=cv2.waitKey(1) & 0xff
    if k==27:#ESC is pressed
        break
cap.release()
cv2.destroyAllWindows()

