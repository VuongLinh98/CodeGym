import turtle 
import random

#khởi tạo đối tượng và đặt vị trí
# căn điểm nhốt rùa là chính giữa màn hình
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0, -300)

#vẽ đường bao nhốt rùa có màu xanh nước biển
t.speed(10)
t.pensize(10)
t.pencolor("blue")
t.pendown()
t.circle(300)

#đặt con trỏ hình rùa về vị trí chính giữa
#đổi màu con rùa thành màu xanh
t.penup()
t.speed(10)
t.fillcolor("green")
t.begin_fill()
t.shape("turtle")
t.pencolor("green")
t.turtlesize(3)
t.end_fill()
t.goto(0, 0)

#tạo hướng ngẫu nhiên ban đầu cho rùa
angle = random.randint(0, 360)
t.left(angle)
t.showturtle()

#bắt đầu cho rùa di chuyển đến đường bao quanh
#mỗi khi chạm đường bao quanh cho rùa trở về vị trí cũ
count = 0
while True:
    t.speed(1)
    t.forward(288)
    t.hideturtle()
    t.speed(10)
    t.goto(0,0)
    t.showturtle()
    angle = random.randint(0, 360)
    t.left(angle)
    count += 1
    if count == 10:
        break

turtle.done()
