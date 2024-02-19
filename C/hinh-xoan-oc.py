import turtle

distance = int(input("Nhập giá trị dừng: "))

t = turtle.Turtle()
t.pensize(3)
t.pencolor("red")

d = 30
while True :
    t.circle(d,180)
    d += 10
    if d >= distance :
        break

turtle.done()
