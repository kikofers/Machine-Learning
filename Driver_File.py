import tensorflow as tf
import keras
from keras.layers import Flatten, Dense, Dropout, Convolution2D, MaxPooling2D
from keras.utils import to_categorical

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

from os import listdir
from numpy import asarray
from numpy import save
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

direktorija = 'training_set/'
bildes, virsraksti = list(), list()

for fails in listdir(direktorija):
    izvade = 0.0
    if fails.startswith('dog'):
        izvade = 1.0
        bilde = load_img(direktorija + fails, target_size=(200, 200))
        bilde = img_to_array(bilde)
        bildes.append(bilde)
        virsraksti.append(izvade)

bildes = asarray(bildes)
virsraksti = asarray(virsraksti)

print(bildes.shape, virsraksti.shape)

save('kakis_suns.npy', bildes)
save('kakis_suns.npy', virsraksti)

"""
# Parādam pirmās 9 bildes. Pārbaudu, vai programma var atrast bildes un direktorija ir korekta.
for i in range(1, 10):
    plt.subplot(330 + i)
    fails = direktorija + 'dog.' + str(i) + '.jpg'
    bilde = imread(fails)
    plt.imshow(bilde)

plt.show()
"""

