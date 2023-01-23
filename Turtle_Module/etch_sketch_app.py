from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)
    # alternatively below, makes us turn left by 10 degrees each time... moves anti-clockwise
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)

def turn_right():
    tim.right(10)
    # alternatively, we can use this below.... moves clockwise
    # new_heading = tim.heading() - 10  
    # tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()  # this returns the turtle back to the initial center
    tim.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()


# in order to draw a circle shape, we can hit W + D key one at a time, repeatedly
# the same concepts goes for any random drawing you have in mind
