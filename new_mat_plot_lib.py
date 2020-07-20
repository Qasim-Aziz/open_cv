import cv2
import matplotlib

import matplotlib.pyplot as plt



img = cv2.imread('lena.png', -1)
cv2.imshow('image', img)

plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

