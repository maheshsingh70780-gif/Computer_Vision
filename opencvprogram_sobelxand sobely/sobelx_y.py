import cv2

img = cv2.imread("opencvprogram_sobelxand sobely/mahesh.jpg")

if img is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

magnitude = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv2.imwrite("output.jpg", magnitude)

cv2.imshow("Input", img)
cv2.imshow("Sobel Edge", magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()