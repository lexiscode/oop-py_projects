from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("tomato4")

tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)

#Alternatively, using for loop
for _ in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()
