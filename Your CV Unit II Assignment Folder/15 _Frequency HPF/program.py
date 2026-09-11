import cv2
import numpy as np

img = cv2.imread("input.jpg", 0)

if img is None:
    print("Error: input.jpg nahi mili!")
    exit()

dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows // 2, cols // 2

mask = np.ones((rows, cols), np.uint8)

radius = 30

cv2.circle(mask, (ccol, crow), radius, 0, -1)

filtered = dft_shift * mask

inverse_shift = np.fft.ifftshift(filtered)

output = np.fft.ifft2(inverse_shift)

output = np.abs(output)

output = cv2.normalize(
    output, None, 0, 255, cv2.NORM_MINMAX
)

output = np.uint8(output)

cv2.imwrite("output.png", output)

cv2.imshow("Original", img)
cv2.imshow("Frequency HPF", output)

cv2.waitKey(0)
cv2.destroyAllWindows()