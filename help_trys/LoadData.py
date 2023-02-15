# https://towardsdatascience.com/covolutional-neural-network-cb0883dd6529
# https://www.youtube.com/watch?v=j-3vuBynnOE

import numpy as np
import os
import cv2
import random
import pickle

DATADIR = r"..\train_images"
Classes = os.listdir(DATADIR)   # ["oranges", "apples" ...]
IMG_SIZE = 150

train_data = []

def create_train_data():
    for fruit in Classes:
        path = os.path.join(DATADIR, fruit)
        for img in os.listdir(path):
            try:
                Classe_num = Classes.index(fruit)
                img_array = cv2.imread(os.path.join(path, img))
                new_img = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                train_data.append([new_img, Classe_num])

            except Exception as e:
                print(e)


print(Classes)
create_train_data()
for i in range(3):
    random.shuffle(train_data)

print(len(train_data), "images uploaded")


X = []
Y = []

for features, labels in train_data:
    X.append(features)
    Y.append(labels)

Y = np.array(Y).reshape(-1, 1)

print("shape of X:", np.shape(X))
print("shape of Y:", np.shape(Y))

pickle_out = open("my_X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("my_Y.pickle", "wb")
pickle.dump(Y, pickle_out)
pickle_out.close()