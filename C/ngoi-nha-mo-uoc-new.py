#thêm thư viện
import turtle

t = turtle.Turtle()
t.pensize(3)
t.speed(10)

#đường nền nhà
t.penup()
t.goto(-170, -230)
t.pendown()
t.pencolor("#6b6155")
t.fillcolor("#6b6155")
t.begin_fill()
for i in range(2):
    t.forward(400)
    t.right(90)
    t.forward(7)
    t.right(90)
t.end_fill()

#mặt trái ngôi nhà
t.penup()
t.forward(40)
t.left(90)
t.pendown()
t.pencolor("#f6e1a0")
t.fillcolor("#f6e1a0")
t.begin_fill()
t.forward(280)
t.right(50)
t.forward(80)
t.right(80)
t.forward(80)
t.right(50)
t.forward(280)
t.end_fill()
#mái trước
t.penup()
t.backward(280)
t.left(50)
t.forward(20)
t.left(180)
t.pendown()
t.pensize(14)
t.pencolor("#77879c")
t.forward(100)
t.left(80)
t.forward(100)

#cửa sổ trước
t.penup()
t.right(180)
t.forward(100)
t.right(130)
t.forward(150)




turtle.done()
