import os
import cv2
import torch
from torch.utils.data import Dataset
from skimage import io
from classesImages import classes_images


class fruits_dataset(Dataset):
    def __init__(self, root_dir, transfrom=None):
        self.root_dir = root_dir
        self.classify = classes_images
        self.transfrom = transfrom

    def __len__(self):
        return len(self.classify)

    def __getitem__(self, index):
        img_path = self.classify[index][0]
        image = io.imread(img_path)
        y_lable = torch.tensor(int(self.classify[index][1]))
        if self.transfrom:
            image = self.transfrom(image)
        return image, y_lable

    def __load_data_to_array__(self):
        ret_list = []
        IMG_SIZE = 150
        classes = os.listdir(self.root_dir)
        for fruit in classes:
            path = os.path.join(self.root_dir, fruit)
            for img in os.listdir(path):
                try:
                    class_num = classes.index(fruit)
                    fruit = os.path.join(self.root_dir, img)
                    ret_list.append((fruit, class_num))

                except Exception as e:
                    print(e)
        return ret_list
