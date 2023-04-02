from keras.models import Sequential
from keras.layers.convolutional import Conv2D
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), padding='same', activation='relu'))
#model.add(Conv2D(32, (3, 3), activation='relu', padding='valid'))
