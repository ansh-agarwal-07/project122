import cv2
import time
import numpy as np

video = cv2.VideoCapture(0)
image = cv2.imread("me.jpg")





while(True):
    ret, img = video.read()
    print(frame)

frame = cv2. resize(frame, (640, 480))
image = cv2. resize(image, (640, 480))
u_black = np. array ( [104, 153, 70])
l_black = np.array ([30, 30, 0])
mask = cv2.inRange (frame, 1 black, u black)
res = cv2.bitwise_and(frame, frame, mask = mask)
f = frame - res
f = np.where(f == 0, image, f)

    cv2.imshow("video",frame)
    cv2.imshow("mask",F)
    cv2.waitKey(1)

video.release()

cv2.destroyAllWindows()
 