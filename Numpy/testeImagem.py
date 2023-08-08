from skimage import io
import numpy as np
import matplotlib.pyplot as plt

img = io.imread('Numpy/skimage.webp')
plt.imshow(img)
print(img)
plt.savefig('imagemSalva.png')
