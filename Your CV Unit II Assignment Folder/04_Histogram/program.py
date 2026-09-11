import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Error: input.jpg nahi mili!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

hist_image = cv2.normalize(hist, None, 0, 400, cv2.NORM_MINMAX)

import numpy as np

canvas = np.zeros((400, 512, 3), dtype=np.uint8)

for i in range(256):
    x1 = i * 2
    x2 = i * 2
    y1 = 400
    y2 = 400 - int(hist_image[i])

    cv2.line(canvas, (x1, y1), (x2, y2), (255, 255, 255), 1)

cv2.imwrite("output.png", canvas)

cv2.imshow("Histogram", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()