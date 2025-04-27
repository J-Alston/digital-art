import HelperFunctions
from PIL import Image, ImageDraw
import numpy as np

#define image parameters
w = 2000
h = 2000
img = Image.new("RGB", (w, h), '#FFFDD0') 

#make an interesting theta field
row_count = 40
column_count = 40
theta_field = []
for i in range(row_count):
    theta_field_row = []
    for j in range(column_count):
        theta_field_row.append(np.sin(i**1.2*np.pi/column_count)+np.cos(0.5*j**1.3*np.pi/column_count))
    theta_field.append(theta_field_row)

#make grid of line objects out of theta field
line_grid = HelperFunctions.line_grid(np.array(theta_field), w, h).line_grid

img1 = ImageDraw.Draw(img)
for row in line_grid:
    for line in row:
        img1.line(line.xy, fill ="gray", width = 5)
img.show()