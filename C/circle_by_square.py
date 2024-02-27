import turtle
t = turtle.Turtle()
t.speed(20)
t.pensize(3)
t.color("red")

def draw_square(d, angle):
    for i in range(3) :
        t.forward(d)
        t.right(90)
    t.forward(d)
    t.right(90 + angle)

d = int(input("Nhập độ dài cạnh hình vuông: "))
step = 36 
angle = 360/step

for i in range(step) :
    draw_square(d, angle)

turtle.done()
