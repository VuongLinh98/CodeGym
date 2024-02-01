import turtle

t=turtle.Turtle()
t.color("red")

t.fillcolor("red")
t.begin_fill()
for i in range(4) :
    t.forward(200)
    t.right(90)
t.end_fill()

turtle.done()