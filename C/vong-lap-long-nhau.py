import turtle

t = turtle.Turtle()
t.speed(10)
t.color("blue")

for i in range(1,100):
    for j in range(1,6):
        t.left(144)
        t.forward(200)
    t.left(5)

turtle.done()
