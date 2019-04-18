import cv2
import numpy as np
from matplotlib import pyplot as plt

# lendo a imagem
img = cv2.imread('placa2.tif') 

#aplicando o filtro na imagem(filtro de media)
blur = cv2.blur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Filtrada')
plt.xticks([]), plt.yticks([])
plt.show()