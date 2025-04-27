import HelperFunctions
from PIL import Image, ImageDraw
import numpy as np

w = 500
h = 500

img = Image.new("RGB", (w, h)) 

line = HelperFunctions.short_line(200,200, 50, np.pi/5)

print(line)
img1 = ImageDraw.Draw(img)   
img1.line(line, fill ="blue", width = 0)
img.show()