import turtle
pen = turtle.Turtle() 
pen.speed(20)

def draw_hcn(CD,CR):
    for i in range(2):
        pen.forward(CD)
        pen.left(90)
        pen.forward(CR)
        pen.left(90)
#nền 1
pen.penup()
pen.goto(-300,-300)
pen.pendown()
pen.fillcolor("#818181")
pen.begin_fill()
draw_hcn(600,30)
pen.end_fill()
#nền 2
pen.penup()
pen.goto(-250,-270)
pen.pendown()
pen.fillcolor("#747474")
pen.begin_fill()
draw_hcn(500,30)
pen.end_fill()
#tường nhà
pen.penup()
pen.goto(-200,-240)
pen.pendown()
pen.fillcolor("#575b64")
pen.begin_fill()
draw_hcn(400,600)
pen.end_fill()
#cửa chính
pen.penup()
pen.goto(-40,-240)
pen.pendown()
pen.pensize(4)
pen.pencolor("#45484f")
pen.fillcolor("#bbdefb")
pen.begin_fill()
draw_hcn(80,100)
pen.end_fill()
#cửa sổ
pen.penup()
y = -100
pen.goto(-170,y)
for j in range(5):
    for i in range(3):
        pen.pendown()
        pen.pensize(4)
        pen.pencolor("#45484f")
        pen.fillcolor("#bbdefb")
        pen.begin_fill()
        draw_hcn(80,80)
        pen.end_fill()
        pen.penup()
        pen.forward(130)
    pen.penup()
    pen.goto(-170, y)
    y+=120
#tầng
pen.penup()
y = -120
pen.goto(-200,y)
pen.pendown()
pen.pencolor("#263238")
for i in range(5):
    pen.forward(400)
    pen.penup()
    pen.goto(-200,y)
    pen.pendown()
    y += 120
#nóc1
pen.penup()
pen.backward(10)
pen.pendown()
pen.pensize(1)
pen.fillcolor("#263238")
pen.begin_fill()
draw_hcn(420,20)
pen.end_fill()
#nóc 2
pen.penup()
pen.goto(-170,380)
pen.pendown()
pen.pensize(1)
pen.fillcolor("#5e636d")
pen.begin_fill()
draw_hcn(340,50)
pen.end_fill()

turtle.done()