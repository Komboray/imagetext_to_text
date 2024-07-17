# we need to install tesseract for my system and launch the exe
# pip install -r requirements.txt
# VIDEO FROM MISHA SV - How To Extract Text From Image Using Python and Tesseract
# with open('requirements.txt', 'w') as f:
#     f.write('pillow\n pytesseract')

from PIL import Image
from pytesseract import pytesseract
import os
# PATH TO THE EXE TESSERACT
path_to_tesseract = r'C:\Users\Raymond\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Define the path to the image
path_to_image = 'images/panadol.png'

#POINT TESSERACT TO THE EXE
pytesseract.tesseract_cmd = path_to_tesseract

# Define the path to the images folder
path_to_images = r'images/'

# Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_images):
    for file_name in file_names:
        img = Image.open(path_to_images + file_name)

        text = pytesseract.image_to_string(img)
        print(text)
