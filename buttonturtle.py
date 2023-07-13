from turtle import Screen, Turtle

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

def draw_onclick(x, y):
    turtle.dot(100, 'cyan')

button = Turtle()
button.hideturtle()
button.shape('circle')
button.fillcolor('red')
button.penup()
button.goto(150, 150)
button.write("Click me!", align='center', font=FONT)
button.sety(150 + CURSOR_SIZE + FONT_SIZE)
button.onclick(draw_onclick)
button.showturtle()

turtle = Turtle()
turtle.hideturtle()

screen = Screen()
screen.mainloop()
