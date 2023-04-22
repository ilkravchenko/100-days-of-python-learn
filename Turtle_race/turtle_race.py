from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Your bet",
                              prompt="How do you think. who will win this race? Enter a colour: ").lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

x = -230
y = -100

for index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=x, y=y)
    y += 40
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turt in all_turtles:
        rand_distance = random.randint(0, 10)
        turt.forward(rand_distance)

        if turt.xcor() > 230:
            is_race_on = False
            winning_color = turt.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost. The {winning_color} is the winner!")

screen.exitonclick()
