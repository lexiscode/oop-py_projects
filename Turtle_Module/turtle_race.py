from turtle import Turtle, Screen
import random


screen = Screen()
screen.bgcolor("black")
screen.title("TURTLE RACE")

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]


all_turtles = []  # this creates a list of object instances
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    # tim.shape("turtle"), no need for this since it's already in the class argument
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 220:
            is_race_on = False  # this stops the whole race once a turtle gets beyond 230
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                # print(f"You've won! The {winning_color} turtle is the winner!")
                turtle.goto(0, 0)
                turtle.write(f"You've won! The {winning_color} turtle is the winner!", align="center", font=("Arial", 14, "normal"))
            else:
                # print(f"You've lost! The {winning_color} turtle is the winner!")
                turtle.goto(0, 0)
                turtle.write(f"You've lost! The {winning_color} turtle is the winner!", align="center", font=("Arial", 14, "normal"))

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()



#DOWNLOAD/PLAY THE GAME ON YOUR WINDOWS PC 
# https://1drv.ms/u/s!AqiJaR7AblSkiQlmS9wH3IEWqw-q
