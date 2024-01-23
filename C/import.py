import math
R = float(input("Nhập độ dài R: "))
S = math.pi*R**2
print("Diện tích hình tròn là: ", S)

import turtle
t = turtle.Turtle()
t.fillcolor("blue")
t.begin_fill()
t.circle(R,360)
t.end_fill()

turtle.done()