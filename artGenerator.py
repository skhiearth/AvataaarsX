from PIL import Image
from textToImage import generateNFT
import random

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width = 150):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    ASCII_CHARS_RANDOM = random.sample(ASCII_CHARS, random.randint(2, len(ASCII_CHARS)))
    if(len(ASCII_CHARS_RANDOM) == 1):
        characters = "".join([ASCII_CHARS_RANDOM[pixel//120] for pixel in pixels])
        return(characters)
    elif(len(ASCII_CHARS_RANDOM) == 2):
        characters = "".join([ASCII_CHARS_RANDOM[pixel//160] for pixel in pixels])
        return(characters)
    elif(len(ASCII_CHARS_RANDOM) == 3):
        characters = "".join([ASCII_CHARS_RANDOM[pixel//95] for pixel in pixels])
        return(characters)
    elif(len(ASCII_CHARS_RANDOM) == 4):
        characters = "".join([ASCII_CHARS_RANDOM[pixel//75] for pixel in pixels])
        return(characters)
    elif(len(ASCII_CHARS_RANDOM) == 5):
        characters = "".join([ASCII_CHARS_RANDOM[pixel//65] for pixel in pixels])
        return(characters)
    elif(len(ASCII_CHARS_RANDOM) == 6):
        characters = "".join([ASCII_CHARS_RANDOM[pixel//50] for pixel in pixels])
        return(characters)
    elif(len(ASCII_CHARS_RANDOM) == 7):
        characters = "".join([ASCII_CHARS_RANDOM[pixel//45] for pixel in pixels])
        return(characters)
    elif(len(ASCII_CHARS_RANDOM) == 8):
        characters = "".join([ASCII_CHARS_RANDOM[pixel//40] for pixel in pixels])
        return(characters)
    elif(len(ASCII_CHARS_RANDOM) == 9):
        characters = "".join([ASCII_CHARS_RANDOM[pixel//35] for pixel in pixels])
        return(characters)
    elif(len(ASCII_CHARS_RANDOM) == 10):
        characters = "".join([ASCII_CHARS_RANDOM[pixel//30] for pixel in pixels])
        return(characters)
    else:
        characters = "".join([ASCII_CHARS_RANDOM[pixel//30] for pixel in pixels])
        return(characters)

def main(number, new_width = 150):
    try:
        image = Image.open("Avatars/avatar{}.png".format(number))
    except:
        print("Invalid path")
        return

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    with open("ASCII/ascii_image{}.txt".format(number), "w") as f:
        f.write(ascii_image)

    generateNFT(number)