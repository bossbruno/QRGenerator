import qrcode
from PIL import Image
import os
# Gets your current project directory
curr_directory = os.getcwd()

# Gets the link the user wants to make a QRCode
data = input("Enter the link you want to make QRCode for \n")

# Create the QRcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create an Image for the QRCode
image = qr.make_image(fill="black", back_color="white")

# Gets the name the user wants to name the image
name = input("What do you want to name your image \n")

# Saves the image with PNG at the end of user provided name in your project directory
pic = image.save(name.__add__(".png"))
picname = name.__add__(".png")

# Opens QRcode image in your preferred Imageviewer
im = Image.open(f"{curr_directory}\\{picname}")
im.show()

