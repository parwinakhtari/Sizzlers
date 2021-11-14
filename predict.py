import pickle
import numpy as np
import pandas as pd
import cv2

loaded_model = pickle.load(open("final_model.sav", "rb"))


def prediction(path):
    new_img = cv2.imread(path)
    img1 = cv2.resize(new_img, (200, 200))
    img = np.mean(img1, axis=2)
    img1 = img.reshape(1, -1) / 255
    pred = loaded_model.predict(img1)[0]
    return pred


l1 = prediction("test1.jpg")
print(l1)
