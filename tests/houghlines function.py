import cv2
import numpy as np
def findCube(croppedImage,horizontalLines,verticalLines,sideThreshold=0.1):
    horRange=max(horizontalLines)-min(horizontalLines)
    verRange=max(verticalLines)-min(verticalLines)
    
    if 0.9*verRange<=horRange<=1.1*verRange:
        return [[min(verticalLines),max(verticalLines)],[min(horixontalLines),max(horixontalLines)]]
    return False

