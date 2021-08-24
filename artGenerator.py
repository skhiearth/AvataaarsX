from PIL import Image
from textToImage import generateNFT

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
    characters = "".join([ASCII_CHARS[pixel//30] for pixel in pixels])
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