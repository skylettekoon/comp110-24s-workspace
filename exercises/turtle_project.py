"""TODO: Describe your scene program."""

from turtle import Turtle, colormode, done
from random import randint

"""To go above and beyond, I decided to fill in all of the shapes with color,
   and I included more than just 4 components. I utilized the randint function in 
   my stars function in order to generate flowers with different shades of pink.
   I also decided to used the circle feature to add more elements to my picture."""

__author__ = "730559378"

colormode(255)


def window(rect: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a rectangle of the given width whose top left corner located at x, y."""
    rect.speed(25)
    rect.hideturtle()
    rect.fillcolor(245, 242, 242)
    rect.begin_fill()
    rect.penup()
    rect.goto(x, y)
    rect.setheading(0.0)
    rect.pendown()
    i: int = 0
    while i < 2:
        rect.forward(width)
        rect.right(90)
        rect.forward(height)
        rect.right(90)
        i = i + 1
    rect.end_fill()


def door(rect: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a rectangle of the given width whose top left corner located at x, y."""
    rect.speed(25)
    rect.hideturtle()
    rect.fillcolor(244, 88, 88)
    rect.begin_fill()
    rect.penup()
    rect.goto(x, y)
    rect.setheading(0.0)
    rect.pendown()
    i: int = 0
    while i < 2:
        rect.forward(width)
        rect.right(90)
        rect.forward(height)
        rect.right(90)
        i = i + 1
    rect.end_fill()


def grass(rect: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a rectangle of the given width whose top left corner located at x, y."""
    rect.speed(25)
    rect.hideturtle()
    rect.color((63, 142, 32), (121, 214, 85))
    rect.begin_fill()
    rect.penup()
    rect.goto(x, y)
    rect.setheading(0.0)
    rect.pendown()
    i: int = 0
    while i < 2:
        rect.forward(width)
        rect.right(90)
        rect.forward(height)
        rect.right(90)
        i = i + 1
    rect.end_fill()


def sky(squr: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of given width whose top left corner is located at x, y."""
    squr.speed(25)
    squr.hideturtle()
    squr.fillcolor(137, 239, 255)
    squr.begin_fill()
    squr.penup()
    squr.goto(x, y)
    squr.setheading(0.0)
    squr.pendown()
    i: int = 0
    while i < 4:
        squr.forward(width)
        squr.left(90)
        i = i + 1
    squr.end_fill()


def square(squr: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of given width whose top left corner is located at x, y."""
    squr.speed(25)
    squr.hideturtle()
    squr.fillcolor(255, 254, 156)
    squr.begin_fill()
    squr.penup()
    squr.goto(x, y)
    squr.setheading(0.0)
    squr.pendown()
    i: int = 0
    while i < 4:
        squr.forward(width)
        squr.left(90)
        i = i + 1
    squr.end_fill()

# Using a randint function to get different shades of pink for the flowers.


def star(twinkle: Turtle, x: float, y: float, width: float) -> None:
    """Draws a star of given width whose location is at x, y."""
    twinkle.speed(25)
    twinkle.hideturtle()
    twinkle.color((255, 6, 116), (237, randint(60, 180), 240))
    twinkle.penup()
    twinkle.goto(x, y)
    twinkle.setheading(35.0)
    twinkle.pendown()
    i: int = 0
    twinkle.begin_fill()
    while i < 6:
        twinkle.forward(width)
        twinkle.left(144)
        i = i + 1
    twinkle.end_fill()


def triangle(tri: Turtle, x: float, y: float, width: float) -> None:
    """Draws a triangle of given width located at x ,y."""
    tri.speed(25)
    tri.hideturtle()
    tri.fillcolor(228, 109, 60)
    tri.begin_fill()
    tri.penup()
    tri.goto(x, y)
    tri.setheading(0.0)
    tri.pendown()
    i: int = 0
    while i < 3:
        tri.forward(width)
        tri.left(120)
        i = i + 1
    tri.end_fill()

# Using a new function: Circle.


def circle(circ: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a circle with the given radius at the given location."""
    circ.speed(25)
    circ.hideturtle()
    circ.color((255, 211, 42), (255, 246, 42))
    circ.begin_fill()
    circ.penup()
    circ.goto(x, y)
    circ.setheading(0.0)
    circ.pendown()
    circ.circle(radius)
    circ.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    squr: Turtle = Turtle()
    sky(squr, -375, -375, 750)
    square(squr, -150, -200, 300)
    rect: Turtle = Turtle()
    window(rect, -90, 20, 55, 75)
    window(rect, 35, 20, 55, 75)
    door(rect, -35, -120, 70, 80)
    grass(rect, -375, -200, 750, 300)
    tri: Turtle = Turtle()
    triangle(tri, -150, 100, 300)
    circ: Turtle = Turtle()
    circle(circ, -250, 150, 75)
    flower_stem_left(3, -330.0, -336.0, -325.0)
    flower_stem_right(3, 200.0, 194.0, 205.0)
    done()

# Recursive Function


def flower_stem_left(n: int, i: float, s: float, c: float) -> None:
    """Makes a series of flowers on the left side of the picture."""
    rect: Turtle = Turtle()
    twinkle: Turtle = Turtle()
    circ: Turtle = Turtle()
    if n == 0:
        return
    else:
        grass(rect, i, - 170, 10, 30)
        star(twinkle, s, - 175, 38)
        circle(circ, c, - 166, 7)
        return flower_stem_left(n - 1, i + 45, s + 45, c + 45)

# Recursive Function


def flower_stem_right(n: int, i: float, s: float, c: float) -> None:
    """Makes a series of flowers on the right side of the picture."""
    rect: Turtle = Turtle()
    twinkle: Turtle = Turtle()
    circ: Turtle = Turtle()
    if n == 0:
        return
    else:
        grass(rect, i, - 170, 10, 30)
        star(twinkle, s, - 175, 38)
        circle(circ, c, - 166, 7)
        return flower_stem_right(n - 1, i + 45, s + 45, c + 45)


if __name__ == "__main__":
    main()