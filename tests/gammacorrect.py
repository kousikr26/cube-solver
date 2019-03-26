
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

gamma=2.0

while(1):

    _, image = cap.read()
    cv2.imshow("org",image)
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    cv2.imshow("gamma",cv2.LUT(image, table))

    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
