from time import sleep
from PIL import Image, ImageOps

import pyscreenshot as ImageGrab
import numpy as np
import pyautogui

#  Click on Reply Button
pyautogui.click(715, 392)

# Box Boundary for catch an obstacle
box = (600, 390, 680, 435)

while True:
    # Grab is like take a screenshot with bbox
    im = ImageGrab.grab(bbox=box)

    # Convert image to Grayscale
    g_im = ImageOps.grayscale(im)

    # Sum all pixels value, normalized by divided by 255.
    sum_ = np.int(np.sum(np.asarray(g_im)/255))
    print("sum: {}".format(sum_))
    if sum_ < 3400:
        # Press "up" key
        sleep(0.01)
        pyautogui.keyDown("up")
        pyautogui.keyUp("up")
