import colorsys
import glob
import os
import random
import sys

from PIL import Image
import numpy as np


def get_brightness(rgb):
    return sum(rgb)/len(rgb)

def get_hue(rgb):
    """
    https://stackoverflow.com/questions/23090019/fastest-formula-to-get-hue-from-rgb
    """
    r, g, b = map(lambda c: c/255, rgb) # We need rgb values between 0 and 1
    return colorsys.rgb_to_hsv(r, g, b)[0]

def play(img):
    pixels = np.asarray(img)
    new_pixels = pixels.copy()
    for idx, row in enumerate(pixels):
        python
        new_pixels[idx] = sorted(row, key=key_func)


def run_for(original_filename):
    inpath = "{}".format(original_filename)
    img = Image.open(inpath)
    play(img)


if __name__ == "__main__":
    for f in glob.glob("inputs/*.jpg"):
        print("running for {}...".format(f))
        run_for(f)
