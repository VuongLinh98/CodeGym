import turtle
import random

pen = turtle.Turtle()
green_colors = ["#2c8d27", "#256f21", "#7e9948", "#3b6c4f", "#c7ce3d"] 
brown_colors = ["#71553f", "#3d1b01", "#967a65", "#523331", "#793d33"]

def draw_tree_circle(CD,CR,R):
    green_color = random.choice(green_colors)
    brown_color = random.choice(brown_colors)
    pen.fillcolor(brown_color)
    pen.pencolor(brown_color)
    for i in range(2):
        pen.begin_fill()
        pen.forward(CD)
        pen.left(90)
        pen.forward(CR)
        pen.left(90)
        pen.end_fill()
    pen.left(90)
    pen.penup()
    pen.forward(CR-20)
    pen.right(90)
    pen.forward(CD/2)
    pen.pendown()
    pen.pencolor(green_color)
    pen.fillcolor(green_color)
    pen.begin_fill()
    pen.circle(R)
    pen.end_fill()

def draw_tree_elip(CD,CR):
    green_color = random.choice(green_colors)
    brown_color = random.choice(brown_colors)
    for i in range(2):
        pen.fillcolor(brown_color)
        pen.pencolor(brown_color)
        pen.begin_fill()
        pen.forward(CD)
        pen.left(90)
        pen.forward(CR)
        pen.left(90)
        pen.end_fill()
    pen.left(90)
    pen.penup()
    pen.forward(CR-20)
    pen.right(90)
    pen.forward(CD+CD/2)
    pen.pendown()
    pen.pencolor(green_color)
    pen.fillcolor(green_color)
    pen.begin_fill()
    for i in range(2) :
        pen.left(45)
        pen.circle(CD*3,90)
        pen.circle(CD*3/2,90)
        pen.right(45)
    pen.end_fill()




