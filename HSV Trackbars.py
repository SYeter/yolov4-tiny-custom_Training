import cv2
import numpy as np
import matplotlib.pyplot as plt

def empty(i):
    pass

path = "dataset_jpg/CELIK-GECIS-DIS-DISLI.dataset_jpg"
cv2.namedWindow("TrackedBars")
cv2.resizeWindow("TrackedBars", 640, 240)


def on_trackbar(red):
    blue_min = cv2.getTrackbarPos("blue Min", "TrackedBars")
    blue_max = cv2.getTrackbarPos("blue Max", "TrackedBars")
    green_min = cv2.getTrackbarPos("green Min", "TrackedBars")
    green_max = cv2.getTrackbarPos("green Max", "TrackedBars")
    red_min = cv2.getTrackbarPos("red Min", "TrackedBars")
    red_max = cv2.getTrackbarPos("red Max", "TrackedBars")

    lower = np.array([blue_min, green_min, red_min])
    upper = np.array([blue_max, green_max, red_max])

    imgMASK = cv2.inRange(imgBGR, lower, upper)
    result = cv2.bitwise_and(imgBGR, imgBGR, mask=imgMASK)

    cv2.imshow("Output1", img)
    cv2.imshow("Output2", imgBGR)
    cv2.imshow("Mask", imgMASK)
    cv2.imshow("result", result)


cv2.createTrackbar("blue Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("blue Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("green Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("green Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("red Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("red Max", "TrackedBars", 255, 255, on_trackbar)

img = cv2.imread(path)
plt.imshow(img)
plt.show()
imgBGR = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# Show some stuff
on_trackbar(0)
# Wait until user press some key
cv2.waitKey()