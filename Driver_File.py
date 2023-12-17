import tensorflow as tf
import keras
from keras.layers import Flatten, Dense, Dropout, Convolution2D, MaxPooling2D
from keras.utils import to_categorical

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

direktorija = 'training_set/'

# Parādam pirmās 9 bildes. Pārbaudu, vai programma var atrast bildes un direktorija ir korekta.
for i in range(1, 10):
    plt.subplot(330 + i)
    fails = direktorija + 'dog.' + str(i) + '.jpg'
    bilde = imread(fails)
    plt.imshow(bilde)

plt.show()