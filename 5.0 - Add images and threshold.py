import cv2
import numpy as np

#images must have the same size
img1 = cv2.imread("road.jpg")
img2 = cv2.imread("car.jpg")

#easier to process cause gray scale(1 channel) is lighter than bgr(3 channels)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#print b1+b2, g1+g2, r1+r2
#sum exceed 255 will remain 255 thus = white
print(img1[0,0])
print(img2[0,0])

#0-1 for the transparency of the images
weighted = cv2.addWeighted(img1, 1, img2, 0.5, 0)

#to take all the picture so threshold like that
#if 170 as threshold, above 170 is white so cant take full picture
#take the white part
ret, mask = cv2.threshold(img2_gray, 252, 255, cv2.THRESH_BINARY_INV)

sum = cv2.add(img2, img2, mask=mask)

cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Sum", sum)
cv2.imshow("weighted", weighted)
cv2.imshow("Image 2 gray", img2_gray)
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
