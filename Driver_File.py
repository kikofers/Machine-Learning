import sys
from keras.utils import to_categorical 
from keras.layers import Flatten, Dense, Convolution2D, MaxPooling2D
from keras.models import Sequential
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
from scipy import misc

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

def secinajums(vesture):
    pyplot.subplot(211)
    pyplot.title('Zaudējums')
    pyplot.plot(vesture.history['loss'], color='blue', label='trenēšana')
    pyplot.plot(vesture.history['val_loss'], color='orange', label='tests')
    pyplot.subplot(212)
    pyplot.title('Precizitāte')
    pyplot.plot(vesture.history['accuracy'], color='blue', label='trenēšana')
    pyplot.plot(vesture.history['val_accuracy'], color='orange', label='tests')
    pyplot.tight_layout()
    pyplot.show()

def testejam():
    modelis = izveido_modeli()
    datagen = ImageDataGenerator(rescale=1.0/255.0)
    # Iedala datus trenēšanas un testēšanas datu kopās.
    trenins = datagen.flow_from_directory("training_set/", class_mode='binary', batch_size=64, target_size=(200, 200))
    tests = datagen.flow_from_directory("test_set/", class_mode='binary', batch_size=64, target_size=(200, 200))
    vesture = modelis.fit(trenins, steps_per_epoch=len(trenins), validation_data=tests, validation_steps=len(tests), epochs=20, verbose=0)
    _, acc = modelis.evaluate_generator(tests, steps=len(tests), verbose=0)
    print('> %.3f' % (acc * 100.0))
    secinajums(vesture)

testejam()
