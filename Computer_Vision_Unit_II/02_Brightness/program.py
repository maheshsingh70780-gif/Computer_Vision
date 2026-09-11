import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Error: input.jpg nahi mili!")
    exit()

brightness = cv2.convertScaleAbs(img, alpha=1.0, beta=50)

cv2.imwrite("output.png", brightness)

cv2.imshow("Original", img)
cv2.imshow("Brightness", brightness)

cv2.waitKey(0)
cv2.destroyAllWindows()