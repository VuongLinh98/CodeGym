import turtle
t = turtle.Turtle()
t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
t.pendown()
for _ in range(5):
    t.forward(70)
    t.right(144)

t.end_fill() 
t.penup()
turtle.done()