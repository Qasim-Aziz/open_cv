import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bunty1.png', cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((2, 2), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=1)
erosion = cv2.erode(mask, kernal, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(4, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# opening = perform erosion followed by  dilation
# closing = perform dilation followed by erosion
# marphological gradient (mg) is differnce between dilation and erosion
# thophat which is differnce between input image and opening
