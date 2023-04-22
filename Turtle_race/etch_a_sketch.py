from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()


def move_forward():
    turt.forward(10)


def move_back():
    turt.back(10)


def clockwise():
    turt.setheading(turt.heading() - 5)


def counter_clockwise():
    turt.setheading(turt.heading() + 5)


def clear_screen():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()

screen.listen()

screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_back)
screen.onkey(key='a',fun=counter_clockwise)
screen.onkey(key='d',fun=clockwise)
screen.onkey(key='c',fun=clear_screen)

screen.exitonclick()
