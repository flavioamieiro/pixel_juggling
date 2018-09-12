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
