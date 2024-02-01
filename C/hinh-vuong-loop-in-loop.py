import turtle
a = int(input("Nhập độ dài cạnh hình vuông: "))

t=turtle.Turtle()
t.color("red")

t.fillcolor("red")
t.begin_fill()
for i in range(4) :
    t.forward(a)
    t.right(90)
t.end_fill()

turtle.done()