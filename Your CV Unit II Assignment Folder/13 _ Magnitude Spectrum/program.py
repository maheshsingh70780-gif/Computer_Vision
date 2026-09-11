import cv2
import numpy as np

img = cv2.imread("input.jpg", 0)

if img is None:
    print("Error: input.jpg nahi mili!")
    exit()

dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

magnitude = 20 * np.log(np.abs(dft_shift) + 1)

magnitude = cv2.normalize(
    magnitude, None, 0, 255, cv2.NORM_MINMAX
)

magnitude = np.uint8(magnitude)

cv2.imwrite("output.png", magnitude)

cv2.imshow("Magnitude Spectrum", magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()