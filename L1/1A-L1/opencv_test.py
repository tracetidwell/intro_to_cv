# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:37:30 2017

@author: Trace
"""

import cv2
import matplotlib.pyplot as plt

print(cv2.__version__)

image = cv2.imread('clouds.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Over the Clouds', image)
#cv2.imshow('Over the Clouds - Gray', gray_image)

print(image.shape)
print(image.dtype)

print(gray_image[101:104, 201:204])
plt.plot(gray_image[101:104, 201:204])
#cv2.waitKey(0)
#cv2.destroyAllWindows