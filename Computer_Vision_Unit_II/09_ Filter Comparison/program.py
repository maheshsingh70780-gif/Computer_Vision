import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Error: input.jpg nahi mili!")
    exit()

mean = cv2.blur(img, (5, 5))
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)

cv2.imwrite("output_mean.png", mean)
cv2.imwrite("output_gaussian.png", gaussian)
cv2.imwrite("output_median.png", median)

cv2.imshow("Original", img)
cv2.imshow("Mean Filter", mean)
cv2.imshow("Gaussian Filter", gaussian)
cv2.imshow("Median Filter", median)

cv2.waitKey(0)
cv2.destroyAllWindows()