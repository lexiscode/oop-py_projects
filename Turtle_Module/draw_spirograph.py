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

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    # remember range() takes integers, and in Python division by default gives a float
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()  # print(tim.heading()) = initializes as 0.0
        tim.setheading(current_heading + size_of_gap)  # creates/sets new headings in the loop increased by gap size

draw_spirograph(2)


screen = Screen()
screen.exitonclick()
