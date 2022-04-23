import turtle
import random

turtle.setup(1280.720)
turtle.bgpic("1233.png")
turtle.speed(1)
turtle.pencolor('white')
turtle.fillcolor('white')


def star_creat():
    turtle.penup()
    turtle.goto(random.randint(-600, 600)), random.randint(-300, 300)
    turtle.pendown()

    s=random.randint(5,11)
    if s%2==1:
        turtle.begin_fill()
        for i in range(s):
            turtle.left(180-180/s)
            turtle.forward(50)
        turtle.end_fill()
for i in range(1000)
    star_creat()
turtle.done    