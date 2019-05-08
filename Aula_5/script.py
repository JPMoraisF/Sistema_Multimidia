from __future__ import print_function
import cv2 as cv
import matplotlib.pyplot as plt


src = cv.imread('mergulhador.jpg')
if src is None:
    print('Could not open or find the image!')
    exit(0)

src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
dst = cv.equalizeHist(src)
cv.imshow('Source image', src)
cv.imshow('Equalized Image', dst)

cv.waitKey()

