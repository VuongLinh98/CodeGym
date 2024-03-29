import turtle

t = turtle.Turtle()
t.pensize(3)
t.pencolor("blue")

t.left(45)
for i in range(2) :
    t.circle(100,90)
    t.circle(50,90)

turtle.done()