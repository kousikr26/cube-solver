import cv2
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    
    


    cv2.imshow("original",frame)
    k=cv2.waitKey(1) & 0xff
    if k==27:#ESC is pressed
        break





cap.release()
cv2.destroyAllWindows()
