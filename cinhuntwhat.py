#cinhunt
import turtle
import random

def gridciaga():
    turtle.speed(5)
    turtle.penup()
    turtle.pensize(2)
    turtle.goto(-50,150)
    turtle.pendown()
    turtle.goto(-50,-150)
    turtle.penup()
    turtle.goto(50,150)
    turtle.pendown()
    turtle.goto(50,-150)
    turtle.penup()
    turtle.goto(-150,50)
    turtle.pendown()
    turtle.goto(150,50)
    turtle.penup()
    turtle.goto(-150,-50)
    turtle.pendown()
    turtle.goto(150,-50)
    turtle.penup()

def turtlex(x,y):
    turtle.goto(x-40,y-40)
    turtle.pendown()
    turtle.goto(x+40,y+40)
    turtle.penup()
    turtle.goto(x-40,y+40)
    turtle.pendown()
    turtle.goto(x+40,y-40)
    turtle.penup()

def turtleo(x,y):
    turtle.goto(x,y-40)
    turtle.pendown()
    turtle.circle(40)
    turtle.penup()

def main():
    CURSOR_SIZE = 20
    FONT_SIZE = 40
    FONT = ('Arial', FONT_SIZE, 'bold')

    gridciaga()
    turtle.pensize(5)
    turtle.goto(0,0)
    turtle.write("aga", font=FONT)
    turtle.goto(3424234234,234234)
turtlex(100,100)
turtleo(-100,-100)