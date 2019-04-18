import cv2
import numpy as np
from matplotlib import pyplot as plt

# lendo a imagem
img = cv2.imread('peppers_gray_ruido.bmp') 

#aplicando o filtro na imagem(filtro de mediana)
blur = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Filtrada')
plt.xticks([]), plt.yticks([])
plt.show()