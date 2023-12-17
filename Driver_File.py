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
from numpy import load

# Kods, kas izveido bildes un virsrakstus .npy failos priekš efektīvākas apstrādes.
"""
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

save('kakis_suns_bildes.npy', bildes)
save('kakis_suns_virsraksti.npy', virsraksti)
"""

# Ielādē bildes un virsrakstus no .npy failiem.
bildes = load('kakis_suns_bildes.npy')
virsraksti = load('kakis_suns_virsraksti.npy')
print(bildes.shape, virsraksti.shape)

# Izveido modeli.
def izveidot_modeli():
    

# Izveido blokus modelim.
model.add(Convolution2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(200, 200, 3)))
model.add(MaxPooling2D((2, 2)))

model.add(Convolution2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(MaxPooling2D((2, 2)))

model.add(Convolution2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(MaxPooling2D((2, 2)))