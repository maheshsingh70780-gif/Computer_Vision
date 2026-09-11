import cv2
import numpy as np

img = cv2.imread(r"c:\Users\computer care\Desktop\coding\02CSS\mahesh.jpeg", 0)
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharp = cv2.filter2D(img, -1, kernel)
blurr = cv2.GaussianBlur(
    img, (5, 5), 0
)  # Iska main kaam image ko blur/smooth karna hai.

#cv2.imshow("original img", img)
#cv2.imshow("Clean Img", blurr)
#cv2.imshow("Gray Scale", img)
#cv2.waitKey(0)
#cv2.distroyAllWindows()

#dft


import cv2
import numpy as np
img = cv2.imread(r"c:\Users\computer care\Desktop\coding\02CSS\mahesh.jpeg", 0)
if image is None:
    print("Image not found!")
    exit()
    dft =cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)

    dft_shitt = np.fft.fftshift(dft)

magnitude = cv2.magenitude(dft_shift[:,:,0],dft_shift[:,:,1])
