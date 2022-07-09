#!/usr/bin/env python3
"""       turtle-example-suite:

            tdemo_yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

"""

import turtle

def yin(cursor, radius, color1, color2):
    cursor.width(3)
    cursor.color("black", color1)
    cursor.begin_fill()
    cursor.circle(radius/2., 180)
    cursor.circle(radius, 180)
    cursor.left(180)
    cursor.circle(-radius/2., 180)
    cursor.end_fill()
    cursor.left(90)
    cursor.up()
    cursor.forward(radius*0.35)
    cursor.right(90)
    cursor.down()
    cursor.color(color1, color2)
    cursor.begin_fill()
    cursor.circle(radius*0.15)
    cursor.end_fill()
    cursor.left(90)
    cursor.up()
    cursor.backward(radius*0.35)
    cursor.down()
    cursor.left(90)

def main(cursor: turtle.RawTurtle):
    cursor.reset()
    yin(cursor, 200, "black", "white")
    yin(cursor, 200, "white", "black")
    cursor.ht()
    return "Done!"
