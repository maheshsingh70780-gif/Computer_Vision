import cv2
import numpy as np

img = cv2.imread("input.jpg")

if img is None:
    print("Error: input.jpg nahi mili!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

min_val = np.min(gray)
max_val = np.max(gray)

output = ((gray - min_val) / (max_val - min_val) * 255).astype(np.uint8)

cv2.imwrite("output.png", output)

cv2.imshow("Original", gray)
cv2.imshow("Contrast Stretching", output)

cv2.waitKey(0)
cv2.destroyAllWindows()