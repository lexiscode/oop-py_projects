from turtle import Turtle, Screen

tim = Turtle()

tim.shape("arrow")

# Triangle Shape
tim.color("tomato4")
tim.forward(100)
tim.right(120)
tim.forward(100)
tim.right(120)
tim.forward(100)
tim.right(120)

# Square Shape
tim.color("chartreuse3")
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)

# Pentagon
tim.color("DarkSlateGrey")
tim.forward(100)
tim.right(72)
tim.forward(100)
tim.right(72)
tim.forward(100)
tim.right(72)
tim.forward(100)
tim.right(72)
tim.forward(100)
tim.right(72)

# Hexagon
tim.color("DeepPink")
tim.forward(100)
tim.right(60)
tim.forward(100)
tim.right(60)
tim.forward(100)
tim.right(60)
tim.forward(100)
tim.right(60)
tim.forward(100)
tim.right(60)
tim.forward(100)
tim.right(60)

# Heptagon
tim.color("DarkOrange")
tim.forward(100)
tim.right(360/7)
tim.forward(100)
tim.right(360/7)
tim.forward(100)
tim.right(360/7)
tim.forward(100)
tim.right(360/7)
tim.forward(100)
tim.right(360/7)
tim.forward(100)
tim.right(360/7)
tim.forward(100)
tim.right(360/7)

# Octagon
tim.color("aquamarine4")
tim.forward(100)
tim.right(45)
tim.forward(100)
tim.right(45)
tim.forward(100)
tim.right(45)
tim.forward(100)
tim.right(45)
tim.forward(100)
tim.right(45)
tim.forward(100)
tim.right(45)
tim.forward(100)
tim.right(45)
tim.forward(100)
tim.right(45)

# Nonagon
tim.color("bisque4")
tim.forward(100)
tim.right(40)
tim.forward(100)
tim.right(40)
tim.forward(100)
tim.right(40)
tim.forward(100)
tim.right(40)
tim.forward(100)
tim.right(40)
tim.forward(100)
tim.right(40)
tim.forward(100)
tim.right(40)
tim.forward(100)
tim.right(40)
tim.forward(100)
tim.right(40)

# Decagon
tim.color("purple")
tim.forward(100)
tim.right(36)
tim.forward(100)
tim.right(36)
tim.forward(100)
tim.right(36)
tim.forward(100)
tim.right(36)
tim.forward(100)
tim.right(36)
tim.forward(100)
tim.right(36)
tim.forward(100)
tim.right(36)
tim.forward(100)
tim.right(36)
tim.forward(100)
tim.right(36)
tim.forward(100)
tim.right(36)


screen = Screen()
screen.exitonclick()


##### ALTERNATIVELY #####

from turtle import Turtle, Screen
import random

# we can import it this way also
# from random import Random
# random = Random()

tim = Turtle()

tim.shape("arrow")

colors = ["tomato4", "chartreuse3", "DarkSlateGrey", "DeepPink", "DarkOrange", "aquamarine4", "bisque4", "purple"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
