from PIL import Image


def crop_image(input_file, output_file):
    im = Image.open(input_file)
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения
    fon_color = pixels[0, 0]
    borders = [x, y, 0, 0]
    for i in range(x):
        for j in range(y):
            pixel = pixels[i, j]
            if pixel != fon_color:
                borders[0] = min(borders[0], i)
                borders[2] = max(borders[2], i)
                borders[1] = min(borders[1], j)
                borders[3] = max(borders[3], j)
    borders[2] += 1
    borders[3] += 1
    cropped_img = im.crop(borders)
    cropped_img.save(output_file)


crop_image('image.png', 'res.png')