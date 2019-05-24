from time import sleep
from PIL import Image, ImageOps

import pyscreenshot as ImageGrab
import numpy as np
import pyautogui

#  Click on Reply Button
pyautogui.click(715, 392)

box = (600, 390, 680, 435)

while True:
    im = ImageGrab.grab(bbox=box)
    g_im = ImageOps.grayscale(im)
    sum_ = np.int(np.sum(np.asarray(g_im)/255))
    print("sum: {}".format(sum_))
    if sum_ < 3400:
        sleep(0.01)
        pyautogui.keyDown("up")
        pyautogui.keyUp("up")

