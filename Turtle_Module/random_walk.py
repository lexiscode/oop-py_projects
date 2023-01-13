#WIKIPEDIA: https://en.wikipedia.org/wiki/Random_walk#Applications


from turtle import Turtle, Screen
import random

tim = Turtle()

#Using Named Specified Colors
colors = ["tomato4", "chartreuse3", "DarkSlateGrey", "DeepPink", "DarkOrange", "aquamarine4", "bisque4", "purple"]
directions = [0, 90, 180, 270]
tim.pensize(15)  # .pensize() is same as .width()
tim.speed("fastest") 

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))  # .setheading() is same as .seth()

screen = Screen()
screen.exitonclick()




## USING RANDOM ALL COLORS - UNSPECIFIED##
#CODE MODIFICATION BELOW

import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

# first modify the turtle module colormode() by setting it from 0-255
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color 

directions = [0, 90, 180, 270]
tim.pensize(15)  # .pensize() is same as .width()
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))  # .setheading() is same as .seth()

screen = Screen()
screen.exitonclick()
