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

from PIL import Image, ImageFilter
import numpy as np

img = Image.open("teste.jpg")

#img.draft("RGB", (400, 300))

scale = 25

pixels = np.asarray(img)
new_pixels = pixels.copy()
num_rows, num_cols, _ = pixels.shape
for i, row in enumerate(pixels[::scale]):
    if i * scale > num_rows - scale:
        continue
    for j, col in enumerate(row[::scale]):
        if j * scale > num_cols - scale:
            continue
        for i_off in range(-scale, scale):
            for j_off in range(-scale, scale):
                new_pixels[i * scale + i_off, j * scale + j_off] = pixels[i*scale,j*scale]
new_img = Image.fromarray(new_pixels)
new_img.save("teste_pixelated.jpg")
new_img.show()
