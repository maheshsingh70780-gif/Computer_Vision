import cv2
import numpy as np

img = cv2.imread("input.jpg")

if img is None:
    print("Error: input.jpg nahi mili!")
    exit()

smooth = cv2.GaussianBlur(img, (5, 5), 0)

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharp = cv2.filter2D(img, -1, kernel)

cv2.imwrite("output_smooth.png", smooth)
cv2.imwrite("output_sharp.png", sharp)

cv2.imshow("Original", img)
cv2.imshow("Smoothing", smooth)
cv2.imshow("Sharpening", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()