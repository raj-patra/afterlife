# File: tdemo_chaos.py
# Author: Gregor Lingl
# Date: 2009-06-24

# A demonstration of chaos

import turtle

N = 80

def f(x):
    return 3.9*x*(1-x)

def g(x):
    return 3.9*(x-x**2)

def h(x):
    return 3.9*x-3.9*x*x

def jumpto(cursor, x, y):
    cursor.penup()
    cursor.goto(x,y)

def line(cursor, x1, y1, x2, y2):
    jumpto(cursor, x1, y1)
    cursor.pendown()
    cursor.goto(x2, y2)

def coosys(cursor):
    line(cursor, -1, 0, N+1, 0)
    line(cursor, 0, -0.1, 0, 1.1)

def plot(cursor, fun, start, color):
    cursor.pencolor(color)
    x = start
    jumpto(cursor, 0, x)
    cursor.pendown()
    cursor.dot(5)
    for i in range(N):
        x=fun(x)
        cursor.goto(i+1,x)
        cursor.dot(5)

def main(cursor: turtle.RawTurtle):
    cursor.reset()
    turtle.setworldcoordinates(-1.0,-0.1, N+1, 1.1)
    cursor.speed(0)
    cursor.hideturtle()
    coosys(cursor)
    plot(cursor, f, 0.35, "blue")
    plot(cursor, g, 0.35, "green")
    plot(cursor, h, 0.35, "red")
    # Now zoom in:
    for s in range(100):
        turtle.setworldcoordinates(0.5*s,-0.1, N+1, 1.1)
    return "Done!"
