import cv2
import numpy as np

img = cv2.imread("lena.png")

layer = img.copy()

guassian_pyramid = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    guassian_pyramid.append(layer)
    #cv2.imshow(str(i), layer)

layer = guassian_pyramid[5]
cv2.imshow('uper level gaussian pyramid', layer)
lp = [layer]

for i in range (5, 0, -1):
    gaussian_extended = cv2.pyrUp(guassian_pyramid[i])
    laplacian = cv2.subtract(guassian_pyramid[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)
    #gaussian_extended = cv2.pyrUp(guassian_pyramid[i])
    #laplacian = cv2.subtract(guassian_pyramid[i-1], gaussian_extended)
    #cv2.imshow(str(i), laplacian)




#lower_resolution = cv2.pyrDown(img)
#lower_resolution1 = cv2.pyrDown(lower_resolution)

#higher_resolution = cv2.pyrUp(lower_resolution1)



cv2.imshow("image", img)


#cv2.imshow("pyr down ", lower_resolution)
#cv2.imshow("pyr down 1", lower_resolution1)
#cv2.imshow("pyr up", higher_resolution)






cv2.waitKey(0)
cv2.destroyAllWindows()
