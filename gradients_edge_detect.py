import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("mesi.jpg", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobel_X = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel_Y = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobel_X = np.uint8(np.absolute(sobel_X))
sobel_Y = np.uint8(np.absolute(sobel_Y))

sobel_combine = cv2.bitwise_or(sobel_X, sobel_Y)



titles = ['image', 'laplasian', 'sobel_X', 'sobel_Y', 'sobel_combine']
images = [img, lap, sobel_X, sobel_Y, sobel_combine]

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()