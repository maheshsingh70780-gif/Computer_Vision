import cv2
import numpy as np

image = cv2.imread(r"Computer_Vision/krishan..jpg",0)

if image is None:
    print("Image not found!")
    exit()

min_value = np.min(image)
max_value = np.max(image)

st = (image - min_value) * (255.0 / (max_value - min_value))
st = st.astype(np.uint8)

cv2.imshow("Original Image", image)
cv2.imshow("Stretched Image", st)

cv2.waitKey(0)
cv2.destroyAllWindows()

