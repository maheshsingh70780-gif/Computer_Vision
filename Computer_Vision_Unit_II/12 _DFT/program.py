import cv2
import numpy as np

img = cv2.imread("input.jpg", 0)

if img is None:print("Error: input.jpg nahi mili!")
exit()

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

magnitude = cv2.magnitude(dft_shift[:, :, 0],
dft_shift[:, :, 1])

magnitude = 20 * np.log(magnitude + 1)

magnitude = cv2.normalize(
    magnitude, None, 0, 255, cv2.NORM_MINMAX
)

magnitude = np.uint8(magnitude)

cv2.imwrite("output.png", magnitude)

cv2.imshow("DFT", magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()