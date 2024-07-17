# we need to install tesseract for my system and launch the exe
# pip install -r requirements.txt
# VIDEO FROM MISHA SV - How To Extract Text From Image Using Python and Tesseract
# with open('requirements.txt', 'w') as f:
#     f.write('pillow\n pytesseract')

from PIL import Image
from pytesseract import pytesseract

# PATH TO THE EXE TESSERACT
path_to_tesseract = r'C:\Users\Raymond\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Define the path to the image
path_to_image = 'images/panadol.png'

#POINT TESSERACT TO THE EXE
pytesseract.tesseract_cmd = path_to_tesseract

#Open the image
img = Image.open(path_to_image)

#extract text from image
text = pytesseract.image_to_string(img)

print(text)
