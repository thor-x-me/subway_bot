"""
This piece of code will help you determine if our model is capturing the right area or not
Run this, it will show you a preview of the area being captured.
"""


import cv2
import numpy as np
import mss
from pynput.keyboard import Controller

mss_instance = mss.mss()
keyboard_instance = Controller()


def get_image_data(scale_percent=20):
    screenshot = mss_instance.grab({
        "left": 1300,
        "top": 0,
        "width": 600,
        "height": 1035
    })
    img_gray = np.array(screenshot)
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    width = int(img_gray.shape[1] * scale_percent / 100)
    height = int(img_gray.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img_gray, dim, interpolation=cv2.INTER_AREA)
    img_blur = cv2.GaussianBlur(resized, (3, 3), 0)
    flattened = img_blur.flatten()
    return img_gray, img_blur, width, height, flattened


while True:

    image, blur, width, height, flattened = get_image_data()

    cv2.imshow("actual_frame", image)
    cv2.imshow("training_frame", blur)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        cv2.destroyAllWidndows()
        break
