# ASCII Art Generator #
from PIL import Image


def generate_ascii_art(image_path, width=80, height=50):
    img = Image.open(image_path).convert('L').resize((width, height))

    chars = '@%#*+=-. '

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            char_index = int(pixel / 255 * len(chars))
            print(chars[char_index], end='')
        print()


image_path = 'C://Users/anuja/OneDrive/Pictures/images/images.jpg'
generate_ascii_art(image_path)