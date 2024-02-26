import turtle

t = turtle.Turtle()
t.pencolor("blue")

def draw(n, d) :
    angle = (n - 2) * 180 / n
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(n) :
        t.forward(d)
        t.right(180 - angle)
    t.end_fill()
    turtle.done()

draw(40, 90)