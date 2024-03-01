import turtle as t
import random

#setup các con tham số
screen = t.Screen()
screen.setup(height=500, width=600)
#Dự đoán chú rùa thắng cuộc
guess = screen.textinput(prompt="Dự đoán con rùa nào chiến thắng?", title="Nhập vào màu rùa (đỏ, nâu, xanh dương, xanh lá cây, cam, hồng)")
# tạo list lưu lại màu của những chú rùa
colors = ["red", "brown", "blue", "green", "orange", "pink"]
# Tạo list vị trí trục y của những chú rùa
y_position = [0, -30, 30, -60, 60, 90]
# Tạo list lưu vận tốc của những chú rùa
#List vận tốc sẽ được dùng ngẫu nhiên khi chọn vận tốc cho các chú rùa
turtle_speed = [10, 15, 20, 25, 30, 5]

# Tạo list lưu các chú rùa
all_turtles = []
run = True

#Tạo hàm để thiết lập vị trí ban đầu, hình chú rùa và màu chú rùa
for turtle in range(0,6) :
    turtles = t.Turtle(shape = 'turtle')
    turtles.penup()
    #di chuyển những chú rùa tới vị trí xuất phát
    turtles.goto(x=-250, y=y_position[turtle])
    #màu của rùa
    turtles.color(colors[turtle])
    #lưu vào list các chú rùa
    all_turtles.append(turtles)

# thiết lập hàm di chuyển về đích của các chú rùa
def random_walk(turtles) :
    global run 
    for turtle in turtles :
        turtle.forward(random.choice(turtle_speed))
        #Khi có 1 chú rùa cán đích thì dừng lại
        if turtle.xcor() > 250:
            run = False

#cho rùa chạy
while run:
    random_walk(all_turtles)

# Chương trình kết thúc khi click chuột lên màn hình
screen.exitonclick()