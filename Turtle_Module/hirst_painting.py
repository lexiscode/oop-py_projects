# Documentation colorgram package: https://pypi.org/project/colorgram.py/
# Hirst Spot painting: https://cdn.cnn.com/cnnnext/dam/assets/200430102527-01-damien-hirst-severed-spots-full-169.jpg

#### FIRSTLY, LETS EXTRACT COLORS FROM AN IMAGE ####

import colorgram

# Extract 30 colors from an image.
colors = colorgram.extract('spot_paintings.jpg', 30)
rgb_colors = []

'''
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)   #test run it
[Rgb(r=253, g=251, b=248), Rgb(r=254, g=250, b=252), Rgb(r=232, g=251, b=242),...]
This print out format isn't really what we can put in a tuple, so lets focus on taking only the values of r, g, and b
using the format of codes below
'''

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# print(rgb_colors)  this prints the kind of tuple format that we need
# [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32),...] which is what is pasted below also in full
'''
Now I selectively delete colors that are white-ish, using their 3 tuple values are numbers very close to 255. I will use the tuple below for the continuation 
of this project. Therefore, the first aim has been achieved successfully, which is to extract colors from an image

[(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), 
 (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), 
 (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
 '''
