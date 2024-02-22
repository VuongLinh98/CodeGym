import turtle

t = turtle.Turtle()
t.pencolor("blue")
t.speed(10)
t.fillcolor("blue")
t.begin_fill()

def square_draw(d) :
    for i in range(4) :
        t.fillcolor("blue")
        t.forward(d)
        t.right(90)
    t.end_fill()
    turtle.done()

square_draw(150)
