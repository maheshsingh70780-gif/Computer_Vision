import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Error: input.jpg nahi mili!")
    exit()

output = cv2.medianBlur(img, 5)

cv2.imwrite("output.png", output)

cv2.imshow("Original", img)
cv2.imshow("Median Filter", output)

cv2.waitKey(0)
cv2.destroyAllWindows()