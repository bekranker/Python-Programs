import cv2
import numpy as np

#We are create a black background.

img = np.zeros((512, 512, 3), np.uint8)

drawing = False
mod = False
x1, yi = -1, -1

def draw(event, x, y, flags, param):

    global drawing, x1, y1
    if event == cv2.EVENT_LBUTTONDOWN:
        print("mouse button down")
        x1, y1 = x, y
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        print("mouse moving")

        if drawing == True:

            if mod:
                cv2.circle(img, (x, y), 10, (100, 50, 0), -1)


            else:
                cv2.line(img, (x, y), (x, y), (102, 0, 153), 5)

        else:
            pass

    elif event == cv2.EVENT_LBUTTONUP:
        print("mouse button  up")



        drawing = False


cv2.namedWindow("point")
cv2.setMouseCallback("point", draw)

while(1):
    cv2.imshow("point", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('m'):
        mod = not mod

cv2.destroyAllWindows()


