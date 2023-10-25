from PIL import Image

image = Image.open("image.bmp")

part_width = image.width // 4
part_height = image.height // 4

for row in range(4):
    for col in range(4):
        left = col * part_width
        upper = row * part_height
        right = (col + 1) * part_width
        lower = (row + 1) * part_height
        part = image.crop((left, upper, right, lower))
        if row == 3 and col == 3:
            continue
        part.save(f"image{row + 1}{col + 1}.bmp")
