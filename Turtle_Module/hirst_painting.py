# About Hirst Paintings: https://www.artsy.net/artist-series/damien-hirst-spots
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





#### THE REAL GOAL OF THE PROJECT IS BELOW #### HIRST PAINTINGS

import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()  # this helps in removing the turtle lines
tim.hideturtle()  # same as using the shortened .ht()

color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

# Let's tweak the position of where the dot should start from in our turtle GUI

tim.setheading(225)  # best positions seems to be within 270 - 360, then I chose to place it at their middle
tim.forward(300)   # we counted this in 50s increments (can be any number like 250), for the dots in our for loop below
tim.setheading(0)  # in order to make takes its new default position in the tweaked position

for dot_count in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        # Now, we want to turn turtle left, with a forward gap of 50, and then turn left again
        tim.left(90)  # is same as this tim.setheading(90)
        tim.forward(50)
        tim.left(90)  # is same as this tim.setheading(180)
        # this below moves our turtle immediately back to the opposite side
        # the forward value is determined by the number of forward dots (which one is 50) present
        tim.forward(500)
        tim.setheading(0)  # sets the turtle head to face right immediately

screen = Screen()
screen.exitonclick()
