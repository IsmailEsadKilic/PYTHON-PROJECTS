import turtle
import math
import time
def draw_axis(a):

    turtle.pensize(2)
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(a, 0)
    turtle.pendown()
    turtle.goto(-a, 0)
    turtle.penup()
    turtle.goto(0, a)
    turtle.pendown()
    turtle.goto(0, -a)
    turtle.penup()


def draw_graph_1(function, scale, decreaser):

    print("grafik çiziliyor...")
    x = -500
    while (x<500):
        y = eval(math.sin(int(function)))
        if round(y*scale*decreaser) > 500 or round(y*scale*decreaser) < -500 or (x*scale) < -500 or (x*scale) > 500:
            print(x * scale, ",", round(y*scale*decreaser), end="    ")
            print("passed")
        else:
            print(x * scale, ",", round(y*scale*decreaser), end="    ")
            print("drawn")
            turtle.goto(x*scale, round(y*scale*decreaser))
            turtle.pendown()
        x += 0.5


def func_name(function):
    turtle.penup()
    turtle.goto(300, -300)
    turtle.pendown()
    turtle.write(function)


def main():
    function = str(input("input the function with x as the variable: \n"))

    scale = int(input("input the zoom amount (default=1): \n"))

    decreaser = float(input("input the coefficinet of y=f(x) (default=1): \n"))

    turtle.speed(10)
    draw_axis(500)
    turtle.speed(4)
    draw_graph_1(function, scale, decreaser)
    func_name(function)
    time.sleep(30)
    return None

main()

