import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

shad = Turtle()
shad.hideturtle()
shad.speed("fastest")
shad.penup()

color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
              (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
              (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31),
              (17, 97, 71)]

shad.setheading(225)
shad.penup()
shad.forward(300)
shad.setheading(0)

for row in range(10):
    for column in range(10):
        shad.dot(20, random.choice(color_list))
        shad.forward(50)
    if int(shad.heading()) == 0:
        shad.left(90)
        shad.forward(50)
        shad.setheading(180)
        shad.forward(500)
        shad.setheading(0)
    else:
        shad.right(90)
        shad.forward(50)
        shad.setheading(0)

screen = Screen()
screen.exitonclick()
