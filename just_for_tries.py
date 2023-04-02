import os, pprint
import cv2
#from classesImages import classes_images

def load_data_to_array():
        ret_list = []
        IMG_SIZE = 150
        classes = os.listdir("train_images")
        for fruit in classes:
            path = os.path.join("train_images", fruit)
            for img in os.listdir(path):
                try:
                    class_num = classes.index(fruit)
                    whole_path = os.path.join(path, img)
                    ret_list.append((whole_path, class_num))

                except Exception as e:
                    print(e)
        saved_file = open("classesImages.py", "w")
        saved_file.write("classes_images = ")
        saved_file.write(pprint.pformat(ret_list))
        saved_file.close()


load_data_to_array()