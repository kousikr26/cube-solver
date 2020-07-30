import cv2
import numpy as np
PI=np.pi
def nothing(x):
    pass
def findCube(croppedImage,horizontalLines,verticalLines,sideThreshold=0.1):
    #print(horizontalLines.shape)
    horRange=max(horizontalLines[:,0])-min(horizontalLines[:,0])
    verRange=max(verticalLines[:,0])-min(verticalLines[:,0])
    
    if 0.9*verRange<=horRange<=1.1*verRange:
        return [[min(verticalLines[:,0]),max(verticalLines[:,0])],[min(horizontalLines[:,0]),max(horizontalLines[:,0])]]
    return []
def removeLines(lines,angleDeviation=0.1):
    newlines=[]
    if lines is not None:
        for line in lines:
            newlines.append(line[0])
        newlines=np.array(newlines)
        #print("in",newlines)
        newlines=newlines[np.logical_or(np.logical_or(newlines[:,1]<angleDeviation,newlines[:,1]>PI-angleDeviation),np.logical_and(newlines[:,1]>PI/2-angleDeviation,newlines[:,1]<PI/2+angleDeviation))]
        horizontalLines=newlines[np.logical_or(newlines[:,1]<angleDeviation,newlines[:,1]>PI-angleDeviation)]
        verticalLines=newlines[np.logical_and(newlines[:,1]>PI/2-angleDeviation,newlines[:,1]<PI/2+angleDeviation)]
        return newlines,horizontalLines,verticalLines
    return np.array([]),np.array([]),np.array([])
cv2.namedWindow('result')
cv2.createTrackbar('cannymin', 'result',210,700,nothing)
cv2.createTrackbar('cannymax', 'result',272,700,nothing)
cv2.createTrackbar('threshold', 'result',114,300,nothing)

cap=cv2.VideoCapture(0)
_,frame=cap.read()
height,width,_=frame.shape


square_size_factor=0.7#fraction of height of image that square occupies
square_x1=int((width-((square_size_factor)*height))/2)#coordinate calculation for square corners
square_x2=int((width+((square_size_factor)*height))/2)


square_y1=int(((1-square_size_factor)/2)*height)
square_y2=int(((1+square_size_factor)/2)*height)
while(1):
    _,img=cap.read()
    cv2.imshow("feed",img)
    
    #img = cv2.imread('cube7.jpg')
    cv2.rectangle(img, (square_x1, square_y1), (square_x2, square_y2), (255,0,0), 2)#cube should be placed within this square
    img=img[square_y1:square_y2,square_x1:square_x2]#image of cube only

    
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cannymin = cv2.getTrackbarPos('cannymin','result')
    cannymax = cv2.getTrackbarPos('cannymax','result')
    threshold = cv2.getTrackbarPos('threshold','result')
    
    edges = cv2.Canny(gray,cannymin,cannymax)
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    cv2.imshow("canny",edges)
    #lines = cv2.HoughLines(edges,rho=0.5,theta=np.pi/80,threshold=90)
    lines = cv2.HoughLines(edges,rho=0.5,theta=np.pi/80,threshold=threshold)
    lines,horizontalLines,verticalLines=removeLines(lines)
    
    

    if horizontalLines.size!=0 and verticalLines.size!=0:
        if findCube(img,horizontalLines,verticalLines)!=[]:
            cubeCoords=findCube(img,horizontalLines,verticalLines)
            print(cubeCoords)
            cv2.imshow("cube",img[int(cubeCoords[1][0]):int(cubeCoords[1][1]),int(cubeCoords[0][0]):int(cubeCoords[0][1])])
        for line in lines:
            rho=line[0]
            theta=line[1]

            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    cv2.imshow('result',img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
