import cv2
image = cv2.imread("input.jpg")
if image is None:
    print("Error: input.jpg nahi mili!")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("output.png", gray)
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Grayscale image successfully saved as output.png")