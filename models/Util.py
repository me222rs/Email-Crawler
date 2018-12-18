from PIL import Image
import pytesseract
from pytesseract import image_to_string
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r''


class Util:

    def __init__(self):
        print("Startar")

    # Returns the text found on the image
    def read_text_on_image(self, img_path):
        print(img_path)
        if img_path.endswith((".png", ".gif")):
            self.gif_to_jpg(img_path)
            return image_to_string(Image.open(img_path), lang='eng')
        return null

    # Convert the image from GIF to JPG
    def gif_to_jpg(self, path):
        Image.open('./images/txt2img.gif').convert('RGB').save('./images/converted.jpg')
        return './images/converted.jpg'

    # print(read_text_on_image(self, "./images/txt2img.gif"))
