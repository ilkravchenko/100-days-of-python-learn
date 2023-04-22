# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('Hirst.png', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
import turtle
import random


def draw_dots(turtle, colors_list):
    x = -200
    y = -200
    for i in range(10):

        for j in range(10):
            turtle.penup()
            turtle.setposition(x, y)
            color = random.choice(colors_list)
            turtle.dot(20, color)

            x += 50

        y += 50
        x = -200


turt = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
screen.screensize(700, 700)
turt.speed(10)
turt.hideturtle()

colors = [(199, 219, 204), (169, 186, 175), (228, 147, 87), (110, 179, 213), (35, 102, 163), (164, 24, 47),
          (173, 166, 32), (218, 127, 152), (181, 199, 186), (191, 224, 235), (50, 26, 48), (221, 211, 73),
          (192, 36, 61), (236, 92, 56), (13, 42, 157), (215, 212, 191), (17, 16, 48), (221, 42, 68), (250, 139, 146),
          (215, 204, 35), (84, 164, 154), (51, 92, 20), (81, 106, 76), (150, 206, 226), (13, 79, 109), (178, 183, 208),
          (59, 149, 161), (120, 86, 65), (59, 94, 18), (231, 167, 161)]

draw_dots(turt, colors)

screen.exitonclick()
