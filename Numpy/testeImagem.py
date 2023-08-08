from skimage import io
import numpy as np      #armazena os pixels da imagem
import matplotlib.pyplot as plt

img = io.imread('Numpy/skimage.webp')

print(img.shape)    #Mostra os pixels

novaImagem = img[0:182] #Exibe apenas os elementos 0 a 181 da matriz
plt.imshow(novaImagem)

plt.savefig('imagemSalva.png')  #Salva a nova imagem cortada

