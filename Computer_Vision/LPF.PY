import cv2
import numpy as np

# 1. Read image
img = cv2.imread(r"c:\Users\computer care\Desktop\coding\02CSS\mahesh.jpeg", 0)

if img is None:
    print("Image not found!")
    exit()

# 2. Get image size
rows, cols = img.shape

# 3. Fourier Transform
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

# 4. Shift low frequencies to center
dft_shift = np.fft.fftshift(dft)

# 5. Create Low Pass Filter mask
crow = rows // 2
ccol = cols // 2

mask = np.zeros((rows, cols, 2), np.uint8)

r = 30

mask[crow-r:crow+r, ccol-r:ccol+r] = 1

# 6. Apply mask
filtered_dft_shift = dft_shift * mask

# 7. Shift frequencies back
filtered_dft = np.fft.ifftshift(filtered_dft_shift)

# 8. Inverse Fourier Transform
img_back = cv2.idft(filtered_dft)

# 9. Calculate magnitude
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# 10. Normalize image
img_back = cv2.normalize( img_back, None, 0, 255, cv2.NORM_MINMAX)

img_back = np.uint8(img_back)

# 11. Display images
cv2.imshow("Original Image", img)
cv2.imshow("Inverse Fourier Image", img_back)

cv2.waitKey(0)
cv2.destroyAllWindows()