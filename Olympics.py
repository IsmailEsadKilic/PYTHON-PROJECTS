import turtle
def halka(x,y,renk):
    turtle.pensize(10)
    turtle.pencolor(renk)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(100)
halka(-200,50,"blue")
halka(-50,50,"black")
halka(100,50,"red")
halka(-125,-25,"yellow")
halka(25,-25,"green")
