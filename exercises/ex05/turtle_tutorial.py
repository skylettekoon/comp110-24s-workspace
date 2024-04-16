"""Turtle tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.penup()
leo.goto(-200, -100)
leo.pendown()
leo.speed(25)
leo.hideturtle()
leo.fillcolor(47, 220, 149)
leo.begin_fill()

# Makes a triangle

i: int = 0
while (i < 3):
    leo.forward(400)
    leo.left(120)
    i = i + 1

leo.end_fill()
done()