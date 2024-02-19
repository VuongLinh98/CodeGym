import turtle
import random as r 

#khởi tạo turtle
t = turtle.Turtle()
t.shape("turtle")
#ẩn hình ảnh rùa
t.hideturtle()
t.pensize(5)
t.color("pink")
t.speed(1)
t.penup()

#Đặt vị trí con rùa sang bên trái 
#so với vị trí giữa màn hình 300 pixel
#mục đích là để con rùa k chạy khỏi màn hình khi vòng lặp quá lớn
t.goto(-400,0)
#hiển thị hình ảnh con rùa
t.showturtle()

count = 0 
while count < 15 :
    #sinh hai giá trị ngẫu nhiên
    down = r.randint(20, 40)
    up = r.randint(20, 40) 
    t.pendown()
    #rùa tiến về phía trước với giá trị ngẫu nhiên ở trên có để lại nét vẽ 
    t.forward(down)
    t.penup()
    #rùa tiến về phía trước ngẫu nhiên không để lại nét vẽ
    t.forward(up)
    count += 1
turtle.done()