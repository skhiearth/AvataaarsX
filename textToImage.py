from math import ceil

from PIL import (
    Image,
    ImageFont,
    ImageDraw,
)

PIL_GRAYSCALE = 'L'
PIL_WIDTH_INDEX = 0
PIL_HEIGHT_INDEX = 1

def generateNFT(number):
    image = textfile_to_image('ASCII/ascii_image{}.txt'.format(number))
    image.save('NFTs/AvataaarsX{}.png'.format(number))

def textfile_to_image(textfile_path):
    with open(textfile_path) as f:
        lines = tuple(line.rstrip() for line in f.readlines())

    font = ImageFont.load_default()

    font_points_to_pixels = lambda pt: round(pt * 20.0 / 26)
    margin_pixels = 20

    tallest_line = max(lines, key=lambda line: font.getsize(line)[PIL_HEIGHT_INDEX])
    max_line_height = font_points_to_pixels(font.getsize(tallest_line)[PIL_HEIGHT_INDEX])
    realistic_line_height = max_line_height * 0.8  
    image_height = int(ceil(realistic_line_height * len(lines) + 2 * margin_pixels))

    widest_line = max(lines, key=lambda s: font.getsize(s)[PIL_WIDTH_INDEX])
    max_line_width = font_points_to_pixels(font.getsize(widest_line)[PIL_WIDTH_INDEX])
    image_width = int(ceil(max_line_width + (12 * margin_pixels)))

    background_color = 255
    image = Image.new(PIL_GRAYSCALE, (image_width, image_height), color=background_color)
    draw = ImageDraw.Draw(image)

    font_color = 0
    horizontal_position = margin_pixels
    for i, line in enumerate(lines):
        vertical_position = int(round(margin_pixels + (i * realistic_line_height)))
        draw.text((horizontal_position, vertical_position), line, fill=font_color, font=font)

    return image