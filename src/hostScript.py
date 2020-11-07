import base64
import time

with open("pizza.jpg", "rb") as img:
    b64img = base64.b64encode(img.read())

#print(my_string.decode('utf-8'))

with open("Img.jpg", "wb") as imgCpy:
    imgCpy.write(base64.b64decode(b64img))