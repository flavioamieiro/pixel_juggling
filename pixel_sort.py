# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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

def sort_pixels_by_func(img, key_func, sort_ratio=1):
    pixels = np.asarray(img)
    new_pixels = pixels.copy()
    for idx, row in enumerate(pixels):
        if random.random() < sort_ratio:
            new_pixels[idx] = sorted(row, key=key_func)
        else:
            new_pixels[idx] = row
    new_img = Image.fromarray(new_pixels)
    return new_img

def swap_channels(img):
    channels = list(img.split())
    channel_swapped = Image.merge("RGB", (channels[2], channels[0], channels[1]))
    return channel_swapped

def run_for(original_filename):
    inpath = "{}".format(original_filename)

    base_filename = os.path.basename(original_filename.rsplit(".", 1)[0])

    get_outpath = lambda suffix: "outputs/{}_{}.jpg".format(base_filename, suffix)


    img = Image.open(inpath)

    if not (len(sys.argv) > 1 and sys.argv[1] == "--high-res"):
        img.draft("RGB", (400, 300))

    img.save(get_outpath("copy"))
    swap_channels(img).save(get_outpath("channel_swapped"))
    sort_pixels_by_func(img, get_brightness, 1).save(get_outpath("sorted_brightness_1"))
    sort_pixels_by_func(img, get_brightness, 0.25).save(get_outpath("sorted_brightness_quarter"))
    sort_pixels_by_func(img, get_hue, 1).save(get_outpath("sorted_hue_1"))
    sort_pixels_by_func(img, get_hue, 0.25).save(get_outpath("sorted_hue_quarter"))


if __name__ == "__main__":
    for f in glob.glob("inputs/*.jpg"):
        print("running for {}...".format(f))
        run_for(f)
