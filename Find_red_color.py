import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread('picture.jpg') # we're opened picture.

while True:
    global red_mask, frame #we need some global variable
    
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # we are changing our picture to HSV color range.
    
    lower_red = np.array([0, 50, 50]) #min. red variable
    upper_red = np.array([0, 255, 255]) #max. red variable
    red_mask = cv2.inRange(frame, lower_red, upper_red) # we are changed our frame variable to black & white

    cv2.imshow("3", red_mask)
    cv2.imshow("2", frame)
    cv2.imshow("1", img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break



cv2.waitKey(0)
cv2.destroyAllWindows()
