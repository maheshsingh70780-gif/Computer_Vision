import cv2
import numpy as np

img = cv2.imread("input.jpg")

if img is None:
    print("Error: input.jpg nahi mili!")
    exit()

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

output = cv2.filter2D(img, -1, kernel)

cv2.imwrite("output.png", output)

cv2.imshow("Original", img)
cv2.imshow("Sharpened", output)

cv2.waitKey(0)
cv2.destroyAllWindows()