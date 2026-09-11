import cv2
import numpy as np
image = cv2.imread(r"c:\Users\computer care\Desktop\coding\02CSS\mahesh.jpeg")
if image is None:
    print("Image not found!")
    exit()
# Mean Blur
mean = cv2.blur(image, (5, 5))
# Gaussian Blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)
# Sharpening
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharpened = cv2.filter2D(image, -1, kernel)
# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Mean Blur", mean)
cv2.imshow("Gaussian Blurred Image", blurred)
cv2.imshow("Sharpened Image", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()




