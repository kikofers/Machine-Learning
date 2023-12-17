from keras.layers import Flatten, Dense, Convolution2D, MaxPooling2D
from keras.models import Sequential
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator

# Izveido modeli.
def izveido_modeli():
    modelis = Sequential()
    modelis.add(Convolution2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(200, 200, 3)))
    modelis.add(MaxPooling2D((2, 2)))
    modelis.add(Flatten())
    modelis.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
    modelis.add(Dense(1, activation='sigmoid'))

    opt = SGD(lr=0.001, momentum=0.9)
    modelis.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
    return modelis

modelis = izveido_modeli()

datagen = ImageDataGenerator(rescale=1.0/255.0)

# Iedala datus trenēšanas un testēšanas datu kopās.

