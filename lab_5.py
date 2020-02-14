from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
import numpy as np
import random

def sp_noise(image,prob):
	output = np.zeros(image.shape,np.uint8)
	thres = 1 - prob 
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			rdn = random.random()
			if rdn < prob:
				output[i][j] = 0
			elif rdn > thres:
				output[i][j] = 255
			else:
				output[i][j] = image[i][j]
	return output

#task1
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

#task5

noise_img = sp_noise(image1,0.05)
cv2.imshow('Noise', noise_img)

if cv2.waitKey(0) & 0xff == 27:  
	cv2.destroyAllWindows()

no_noise_img = cv.fastNlMeansDenoisingMulti(noise_img, 2, 5, None, 4, 7, 35)
cv2.imshow('No noise', no_noise_img)

if cv2.waitKey(0) & 0xff == 27:  
	cv2.destroyAllWindows()

#task6
matrix = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(image1, matrix, iterations=1)
img_dilation = cv2.dilate(image1, matrix, iterations=1)
img_opening = cv2.morphologyEx(image1, cv2.MORPH_OPEN, matrix)
img_closing = cv2.morphologyEx(image1, cv2.MORPH_CLOSE, matrix)

cv2.imshow('Erosion', img_erosion)

if cv2.waitKey(0) & 0xff == 27:  
	cv2.destroyAllWindows()

cv2.imshow('Dilation', img_dilation)

if cv2.waitKey(0) & 0xff == 27:  
	cv2.destroyAllWindows()

cv2.imshow('Opening', img_opening)

if cv2.waitKey(0) & 0xff == 27:  
	cv2.destroyAllWindows()

cv2.imshow('Closing', img_closing)

if cv2.waitKey(0) & 0xff == 27:  
	cv2.destroyAllWindows()
