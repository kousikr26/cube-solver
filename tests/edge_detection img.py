import cv2


img = cv2.imread('cube4.jpg')
#img=cv2.medianBlur(img,15)
cv2.imshow('imageorg', img)
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
edges = cv2.Canny(hsv, 10, 600)
new=img.copy()

img2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(new,contours,-1,(0,0,255),3)
image = 0

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True) #Removes tiny deviations, tries to go for straight lines.
    if len(approx) == 4: #Lines, should be square.
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 100:
            print("Width and height: ", w, h)
            image = img[y:y+h, x:x+w]
            print("sq found")
        else:
            print("no sq found")

cv2.imshow('image', new)
cv2.imshow('edges', edges)
cv2.imshow('area', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
