import cv2
import matplotlib.pyplot as plt

img = cv2.imread('fruits.png')
color = ('b', 'g', 'r')

for i,col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist,color=col)
    plt.xlim([0, 256])

plt.show()

#teste = cv2.calcHist([img], [0], None, [256], [0, 256])