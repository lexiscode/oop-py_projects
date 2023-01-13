#WIKIPEDIA: https://en.wikipedia.org/wiki/Random_walk#Applications

from turtle import Turtle, Screen
import random

tim = Turtle()

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
