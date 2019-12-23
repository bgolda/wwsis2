import cv2
import numpy as np

image1 = cv2.imread('./Lab5_imgs/lion.jpg')
image2 = cv2.imread('./Lab5_imgs/color.jpg')

weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
cv2.imshow('Weighted Image', weightedSum)

# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  
	cv2.destroyAllWindows()

subtraction = cv2.subtract(image1, image2)
cv2.imshow('Subtracted Image', subtraction)

if cv2.waitKey(0) & 0xff == 27:  
	cv2.destroyAllWindows()

bitwise_and = cv2.bitwise_and(image1, image2, mask = None)
cv2.imshow('Bitwise And', bitwise_and)

if cv2.waitKey(0) & 0xff == 27:  
	cv2.destroyAllWindows()

bitwise_or = cv2.bitwise_or(image1, image2, mask = None)
cv2.imshow('Bitwise Or', bitwise_or)

if cv2.waitKey(0) & 0xff == 27:  
	cv2.destroyAllWindows()
	
bitwise_xor = cv2.bitwise_xor(image1, image2, mask = None)
cv2.imshow('Bitwise XOr', bitwise_xor)

if cv2.waitKey(0) & 0xff == 27:  
	cv2.destroyAllWindows()
	