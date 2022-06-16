import turtle
import tkinter as tk


def press():
    # star
    # while True:
    #     my_lovely_turtle.forward(200)
    #     my_lovely_turtle.left(170)
    #     if abs(my_lovely_turtle.pos()) < 1:
    #         break
    
    
    for i in range(100):
        my_lovely_turtle.circle(5*i)
        my_lovely_turtle.circle(-5*i)
        my_lovely_turtle.left(i)
    my_lovely_turtle.clear()


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root)
    canvas.config(width=600, height=200)
    canvas.pack(side=tk.LEFT)
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("cyan")
    button = tk.Button(root, text="Press me", command=press)
    button.pack()
    my_lovely_turtle = turtle.RawTurtle(screen, shape="turtle")
    root.mainloop()
