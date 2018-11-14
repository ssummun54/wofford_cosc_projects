#################################################
# flower.py
#   Click and draw any number of flowers.
#################################################
#   Author: Beau Christ
#   Date: 9/24/2017
#################################################

# import libraries
import turtle
import random

# draw the petals of a flower
def bloom(tortoise, fcolor, length):
    tortoise.pencolor('red')
    tortoise.fillcolor(fcolor)
    tortoise.begin_fill()
    for segment in range(8):
        tortoise.forward(length)
        tortoise.left(135)
    tortoise.end_fill()

# draw the stem of a flower
def stem(tortoise, length):
    tortoise.pencolor('green')
    tortoise.pensize(length / 20)
    tortoise.up()
    tortoise.forward(length / 2)
    tortoise.down()
    tortoise.right(90)
    tortoise.forward(length)

# draw a flower
def flower(tortoise, fcolor, length):
    bloom(tortoise, fcolor, length)
    stem(tortoise, length)

# generate a flower with a random size and color
def growFlower(x,y):
    span = random.randrange(20, 200)
    fill = random.choice(['yellow', 'pink', 'red', 'purple'])
    tortoise = turtle.Turtle()
    tortoise.hideturtle()
    tortoise.speed(6)
    tortoise.up()
    tortoise.goto(x,y)
    tortoise.setheading(0)
    tortoise.pensize(1)
    tortoise.down()
    flower(tortoise, fill, span)

# create a Turtle, then initialize the main loop of the program
george = turtle.Turtle()
george.hideturtle()
screen = george.getscreen()
screen.onclick(growFlower)
screen.mainloop()