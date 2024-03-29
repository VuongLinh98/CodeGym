lua_chon = input("Bạn muốn chọn vẽ cảnh buổi nào? Nhập 'sáng' hoặc 'tối'")

if lua_chon == 'sáng' or lua_chon == 'tối':

    import turtle
    import random
    import draw_cloud

    pen = turtle.Turtle()
    pen.speed(40)
    pen.hideturtle()

    #Hàm vẽ hình 
    def draw_hcn(CD,CR):
        for i in range(2):
            pen.forward(CD)
            pen.left(90)
            pen.forward(CR)
            pen.left(90)

    def move_pen(x,y):
        pen.penup()
        pen.goto(x,y)
        pen.pendown()

    def draw_square_trapezoid(x,y,canh_day1,canh_vuong,canh_day2):
        pen.penup()
        pen.goto(x,y)
        pen.pendown()
        pen.forward(canh_day1)
        pen.left(90)
        pen.forward(canh_vuong)
        pen.left(90)
        pen.forward(canh_day2)
        pen.goto(x,y)

    def draw_star(size,col):
        pen.fillcolor(col)
        pen.begin_fill()
        pen.pencolor(col)
        pen.pensize(1)
        for i in range(5):
            pen.forward(size)
            pen.left(72)
            pen.forward(size)
            pen.right(144)
        pen.end_fill()
            
            
            # hàm vẽ cây
    green_colors = ["#2c8d27", "#256f21", "#7e9948", "#3b6c4f", "#c7ce3d"] 
    brown_colors = ["#71553f", "#3d1b01", "#967a65", "#523331", "#793d33"]

    def draw_tree_circle(CD,CR,R):
        green_color = random.choice(green_colors)
        brown_color = random.choice(brown_colors)
        pen.fillcolor(brown_color)
        pen.pencolor(brown_color)
        for i in range(2):
            pen.begin_fill()
            pen.forward(CD)
            pen.left(90)
            pen.forward(CR)
            pen.left(90)
            pen.end_fill()
        pen.left(90)
        pen.penup()
        pen.forward(CR-20)
        pen.right(90)
        pen.forward(CD/2)
        pen.pendown()
        pen.pencolor(green_color)
        pen.fillcolor(green_color)
        pen.begin_fill()
        pen.circle(R)
        pen.end_fill()

    def draw_tree_elip(CD,CR):
        green_color = random.choice(green_colors)
        brown_color = random.choice(brown_colors)
        for i in range(2):
            pen.fillcolor(brown_color)
            pen.pencolor(brown_color)
            pen.begin_fill()
            pen.forward(CD)
            pen.left(90)
            pen.forward(CR)
            pen.left(90)
            pen.end_fill()
        pen.left(90)
        pen.penup()
        pen.forward(CR-20)
        pen.right(90)
        pen.forward(CD+CD/2)
        pen.pendown()
        pen.pencolor(green_color)
        pen.fillcolor(green_color)
        pen.begin_fill()
        for i in range(2) :
            pen.left(45)
            pen.circle(CD*3,90)
            pen.circle(CD*3/2,90)
            pen.right(45)
        pen.end_fill()



    #Vẽ nền trời
    if lua_chon == 'sáng':
        #nền trời sáng
        move_pen(-900,-210)
        pen.pencolor("#dceefc")
        pen.fillcolor("#dceefc")
        pen.begin_fill()
        draw_hcn(1800,600)
        pen.end_fill()
    elif lua_chon == 'tối':
        #nền trời tối
        move_pen(-900,-210)
        pen.pencolor("#182744")
        pen.fillcolor("#182744")
        pen.begin_fill()
        draw_hcn(1800,600)
        pen.end_fill()
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại!")

    #mặt trời
    if lua_chon == 'sáng':
        #mặt trời sáng
        move_pen(550,220)
        pen.pencolor("#ffdd6f")
        pen.fillcolor("#ffdd6f")
        pen.begin_fill()
        pen.circle(60)
        pen.end_fill()
    elif lua_chon == 'tối':
        #mặt trăng
        move_pen(550,220)
        pen.pencolor("#eaea94")
        pen.fillcolor("#eaea94")
        pen.begin_fill()
        pen.circle(60)
        pen.end_fill()
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại!")

    #mây
    if lua_chon == 'sáng':
        #mây sáng
        draw_cloud.penup()
        draw_cloud.goto(50,190)
        draw_cloud.cloud1(40,"#ffffff")

        draw_cloud.penup()
        draw_cloud.goto(380,25)
        draw_cloud.cloud2(50,"#ffffff")

        draw_cloud.penup()
        draw_cloud.goto(250,335)
        draw_cloud.cloud1(60,"#ffffff")

        draw_cloud.penup()
        draw_cloud.goto(500,10)
        draw_cloud.cloud1(30,"#ffffff")

        draw_cloud.penup()
        draw_cloud.goto(-400,190)
        draw_cloud.cloud2(50,"#ffffff")

        draw_cloud.penup()
        draw_cloud.goto(-360,50)
        draw_cloud.cloud2(60,"#ffffff")

        draw_cloud.penup()
        draw_cloud.goto(500,200)
        draw_cloud.cloud2(120,"#ffffff")
    elif lua_chon == 'tối':
        #mây tối
        draw_cloud.penup()
        draw_cloud.goto(50,190)
        draw_cloud.cloud1(40,"#1b395f")

        draw_cloud.penup()
        draw_cloud.goto(380,25)
        draw_cloud.cloud2(50,"#1b395f")

        draw_cloud.penup()
        draw_cloud.goto(250,335)
        draw_cloud.cloud1(60,"#1b395f")

        draw_cloud.penup()
        draw_cloud.goto(500,10)
        draw_cloud.cloud1(30,"#1b395f")

        draw_cloud.penup()
        draw_cloud.goto(-400,190)
        draw_cloud.cloud2(50,"#1b395f")

        draw_cloud.penup()
        draw_cloud.goto(-440,50)
        draw_cloud.cloud2(60,"#1b395f")

        draw_cloud.penup()
        draw_cloud.goto(500,200)
        draw_cloud.cloud2(120,"#1b395f")

        #sao
        for i in range(30):
            x = random.randint(-550, 550)
            y = random.randint(0, 500)
            size = random.randint(2,4)
            move_pen(x, y)
            draw_star(size,"#eaea94")
        # move_pen(-90,160)
        # draw_star(3,"#eaea94")

        # move_pen(-200,190)
        # draw_star(3,"#eaea94")

        # move_pen(-250,170)
        # draw_star(3,"#eaea94")

        # move_pen(-320,230)
        # draw_star(3,"#eaea94")

        # move_pen(-400,220)
        # draw_star(2,"#eaea94")

        # move_pen(-350,290)
        # draw_star(3,"#eaea94")

        # move_pen(250,200)
        # draw_star(3,"#eaea94")

        # move_pen(50,280)
        # draw_star(3,"#eaea94")

        # move_pen(60,290)
        # draw_star(3,"#eaea94")

        # move_pen(40,300)
        # draw_star(2,"#eaea94")

        # move_pen(-400,50)
        # draw_star(2,"#eaea94")

        # move_pen(-500,100)
        # draw_star(3,"#eaea94")

        # move_pen(-400,220)
        # draw_star(2,"#eaea94")

    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")



    #nhà mái vòm
        #tường
    move_pen(80,-200)
    pen.pencolor("#c3d4ce")
    pen.fillcolor("#c3d4ce")
    pen.begin_fill()
    draw_hcn(110,295)
    pen.end_fill()

    move_pen(90,-200)
    for i in range(5):
        pen.pencolor("#317d8d")
        pen.fillcolor("#317d8d")
        pen.begin_fill()
        draw_hcn(10,280)
        pen.end_fill()
        pen.penup()
        pen.forward(20)
        pen.pendown()
        
        #mái
    move_pen(90,95)
    pen.pencolor("#838584")
    pen.fillcolor("#838584")
    pen.begin_fill()
    draw_hcn(90,4)
    pen.end_fill()

    move_pen(90,100)
    pen.pencolor("#c3d4ce")
    pen.fillcolor("#c3d4ce")
    pen.begin_fill()
    draw_hcn(90,35)
    pen.end_fill()

    move_pen(100,105)
    for i in range(4):
        pen.pencolor("#317d8d")
        pen.fillcolor("#317d8d")
        pen.begin_fill()
        draw_hcn(10,25)
        pen.end_fill()
        pen.penup()
        pen.forward(20)
        pen.pendown()

    move_pen(160,134)
    pen.left(90)
    pen.pencolor("#c3d4ce")
    pen.fillcolor("#c3d4ce")
    pen.begin_fill()
    pen.circle(25,180)
    pen.end_fill()
    pen.left(90)

    pen.penup()
    pen.forward(25)
    pen.left(90)
    pen.forward(25)
    pen.pendown()
    pen.pencolor("#c3d4ce")
    pen.pensize(5)
    pen.forward(15)
    pen.right(90)



    #nhà nóc đỏ
    pen.pensize(1)
            #tường 
    move_pen(-50,-200)
    pen.pencolor("#6b94c0")
    pen.fillcolor("#6b94c0")
    pen.begin_fill()
    draw_hcn(165,210)
    pen.end_fill()
        #cửa chính
    move_pen(8,-200)
    pen.pencolor("#c7e4e8")
    pen.fillcolor("#c7e4e8")
    pen.begin_fill()
    draw_hcn(50,40)
    pen.end_fill()

    move_pen(0,-160)
    pen.pencolor("#6389ad")
    pen.fillcolor("#6389ad")
    pen.begin_fill()
    draw_hcn(66,10)
    pen.end_fill()
        #cửa sổ
    y = -125
    move_pen(-30,y)
    for i in range(3):
        for j in range(3):
            pen.pencolor("#cee1e8")
            pen.fillcolor("#cee1e8")
            pen.begin_fill()
            draw_hcn(25,25)
            pen.end_fill()
            pen.penup()
            pen.forward(50)
            pen.pendown()
        pen.penup()
        pen.goto(-30,y+40)
        y+=40
        #nóc
    move_pen(-63,10)
    pen.pencolor("#e0674c")
    pen.fillcolor("#e0674c")
    pen.begin_fill()
    draw_hcn(190,25)
    pen.end_fill()



    #nhà xanh bên phải
    pen.right(90)
    pen.pencolor("#51bcb4")
    pen.fillcolor("#51bcb4")
    pen.begin_fill()
    draw_square_trapezoid(220,-45,155,110,195)
    pen.end_fill()
    pen.right(90)

        #cửa kính
    move_pen(230,-190)
    a = 120
    b = 125
    for i in range(4):
        pen.pencolor("#ace9fc")
        pen.fillcolor("#ace9fc")
        pen.begin_fill()
        pen.left(90)

        pen.forward(a)
        pen.right(70)
        pen.forward(15)
        pen.right(110)
        
        pen.forward(b)
        pen.right(90)
        pen.forward(15)
        pen.right(180)
        pen.end_fill()
        pen.penup()
        pen.forward(25)
        pen.pendown()
        a += 10
        b += 10

    move_pen(230,-60)
    pen.left(21)
    pen.pencolor("#317d73")
    pen.pensize(1.5)
    pen.forward(90)
    pen.right(21)

    move_pen(230,-52)
    pen.pencolor("#317d73")
    pen.fillcolor("#317d73")
    pen.begin_fill()
    pen.left(90)
    pen.forward(5)
    pen.right(70)
    pen.forward(90)
    pen.right(110)
    pen.forward(5)
    pen.right(70)
    pen.forward(90)
    pen.left(160)
    pen.end_fill()
        #mặt trước
    move_pen(328,-200)
    pen.pencolor("#337c73")
    pen.fillcolor("#337c73")
    pen.begin_fill()
    draw_hcn(35,194)
    pen.end_fill()
        #cửa sổ trước
    move_pen(333,-190)
    for i in range(5):
        pen.pencolor("#cee1e8")
        pen.fillcolor("#cee1e8")
        pen.begin_fill()
        draw_hcn(25,25)
        pen.end_fill()
        pen.left(90)
        pen.penup()
        pen.forward(35)
        pen.pendown()
        pen.right(90)



    #nhà tím
        #nền
    move_pen(50,-190)
    pen.pencolor("#848484")
    pen.fillcolor("#848484")
    pen.begin_fill()
    draw_hcn(190,10)
    pen.end_fill()

    move_pen(30,-200)
    pen.pencolor("#443659")
    pen.fillcolor("#443659")
    pen.begin_fill()
    draw_hcn(240,10)
    pen.end_fill()
        #tường
    move_pen(55,-180)
    pen.pencolor("#656aaa")
    pen.fillcolor("#656aaa")
    pen.begin_fill()
    draw_hcn(180,115)
    pen.end_fill()

    move_pen(55,-65)
    pen.pencolor("#4e5281")
    pen.fillcolor("#4e5281")
    pen.begin_fill()
    draw_hcn(180,5)
    pen.end_fill()
        #cửa chính
    move_pen(120,-180)
    pen.pencolor("#4e5281")
    pen.fillcolor("#4e5281")
    pen.begin_fill()
    draw_hcn(50,25)
    pen.end_fill()

    move_pen(145,-180)
    pen.pencolor("#f7f7f8")
    pen.left(90)
    pen.forward(25)
    pen.right(90)

        #cửa sổ
    y = -140
    move_pen(75,y)
    for j in range(3):
        for i in range(2):
            pen.pencolor("#c7e5e5")
            pen.fillcolor("#c7e5e5")
            pen.begin_fill()
            draw_hcn(65,10)
            pen.end_fill()
            pen.penup()
            pen.forward(75)
            pen.pendown()
        pen.penup()
        pen.goto(75,y+25)
        y+=25

        #nóc
    move_pen(45,-60)
    pen.pencolor("#605887")
    pen.fillcolor("#605887")
    pen.begin_fill()
    draw_hcn(200,10)
    pen.end_fill()


    #nhà xám sau cùng
        #tường
    pen.right(90)
    pen.pencolor("#697c8a")
    pen.fillcolor("#697c8a")
    pen.begin_fill()
    draw_square_trapezoid(-185,100,300,85,320)
    pen.end_fill()
    pen.right(90)

        #cửa sổ
    y = -180
    move_pen(-180, y)
    for i in range(13):
        for j in range(4):
            pen.pencolor("#98b5c5")
            pen.fillcolor("#98b5c5")
            pen.begin_fill()
            draw_hcn(5,10)
            pen.end_fill()
            pen.penup()
            pen.forward(20)
            pen.pendown()
        pen.penup()
        pen.goto(-180,y+20)
        y+=20

    y1 = -180
    move_pen(-170, y1)
    for i in range(13):
        for j in range(4):
            pen.pencolor("#98b5c5")
            pen.fillcolor("#98b5c5")
            pen.begin_fill()
            draw_hcn(2,10)
            pen.end_fill()
            pen.penup()
            pen.forward(20)
            pen.pendown()
        pen.penup()
        pen.goto(-170,y1+20)
        y1+=20

        #nóc
    pen.right(90)
    pen.pencolor("#cee1e8")
    pen.fillcolor("#cee1e8")
    pen.begin_fill()
    draw_square_trapezoid(-180,95,15,75,35)
    pen.end_fill()
    pen.right(90)

            #ngang
    move_pen(-180,89)
    pen.pencolor("#697c8a")
    pen.forward(75) 
    move_pen(-180,98)
    pen.forward(75)
    move_pen(-144,107)
    pen.forward(39)
            #dọc
    move_pen(-162,79)
    pen.left(90)
    pen.forward(23) 
    move_pen(-144,79)
    pen.forward(26)
    move_pen(-126,79)
    pen.forward(33)
    pen.right(90)


    #nhà xám bên trái
        #tường
    pen.right(90)
    pen.pencolor("#697c8a")
    pen.fillcolor("#697c8a")
    pen.begin_fill()
    draw_square_trapezoid(-345,180,380,110,350)
    pen.end_fill()
    pen.right(90)

        #cửa sổ
    y = -190
    move_pen(-335, y)
    for i in range(14):
        for j in range(2):
            pen.pencolor("#98b5c5")
            pen.fillcolor("#98b5c5")
            pen.begin_fill()
            draw_hcn(5,10)
            pen.end_fill()
            pen.penup()
            pen.forward(25)
            pen.pendown()
        pen.penup()
        pen.goto(-335,y+23)
        y+=23

    y1 = -190
    move_pen(-325, y1)
    for i in range(14):
        for j in range(2):
            pen.pencolor("#98b5c5")
            pen.fillcolor("#98b5c5")
            pen.begin_fill()
            draw_hcn(5,10)
            pen.end_fill()
            pen.penup()
            pen.forward(25)
            pen.pendown()
        pen.penup()
        pen.goto(-325,y1+23)
        y1+=23

        #nóc
    pen.right(90)
    pen.pencolor("#cee1e8")
    pen.fillcolor("#cee1e8")
    pen.begin_fill()
    draw_square_trapezoid(-340,175,50,100,23)
    pen.end_fill()
    pen.right(90)

            # kẻ ngang
    move_pen(-340,163)
    pen.pencolor("#697c8a")
    pen.forward(48) 
    move_pen(-340,151)
    pen.forward(93)
    move_pen(-340,139)
    pen.forward(105)
            #kẻ dọc
    move_pen(-315,125)
    pen.left(90)
    pen.forward(45) 
    move_pen(-290,125)
    pen.forward(37)
    move_pen(-265,125)
    pen.forward(30)
    pen.right(90)
            #cột vàng
    pen.right(90)
    pen.pencolor("#697c8a")
    pen.fillcolor("#697c8a")
    pen.begin_fill()
    draw_square_trapezoid(-235,150,350,15,315)
    pen.end_fill()
    pen.right(90)

    move_pen(-280,-200)
    for i in range(2):
        pen.pencolor("#e3d7c1")
        pen.fillcolor("#e3d7c1")
        pen.begin_fill()
        draw_hcn(20,320)
        pen.end_fill()
        pen.penup()
        pen.forward(27)
        pen.pendown()
    move_pen(-225,-200)
    pen.pencolor("#e3d7c1")
    pen.fillcolor("#e3d7c1")
    pen.begin_fill()
    draw_hcn(12,320)
    pen.end_fill()
    pen.penup()
            #cột đen
    move_pen(-277,-200)
    for i in range(2):
        pen.pencolor("#697c8a")
        pen.fillcolor("#697c8a")
        pen.begin_fill()
        draw_hcn(3,317)
        pen.end_fill()
        pen.penup()
        pen.forward(10)
        pen.pendown()

    move_pen(-250,-200)
    for i in range(2):
        pen.pencolor("#697c8a")
        pen.fillcolor("#697c8a")
        pen.begin_fill()
        draw_hcn(3,317)
        pen.end_fill()
        pen.penup()
        pen.forward(10)
        pen.pendown()

    move_pen(-222,-200)
    pen.pencolor("#697c8a")
    pen.fillcolor("#697c8a")
    pen.begin_fill()
    draw_hcn(3,317)
    pen.end_fill()


    #bệnh viện
        #tường 2 bên
        #tường trái bệnh viện
    move_pen(-280,-200)
    pen.pencolor("#61a898")
    pen.fillcolor("#61a898")
    pen.begin_fill()
    draw_hcn(65,105)
    pen.end_fill()
        #cửa sổ
    move_pen(-270,-190)
    for i in range(4):
        pen.pencolor("#dbeede")
        pen.fillcolor("#dbeede")
        pen.begin_fill()
        draw_hcn(45,13)
        pen.end_fill()
        pen.penup()
        pen.left(90)
        pen.forward(25)
        pen.pendown()
        pen.right(90)
        pen.penup()
        #nóc
    move_pen(-285,-95)
    pen.pencolor("#407b7a")
    pen.fillcolor("#407b7a")
    pen.begin_fill()
    draw_hcn(75,10)
    pen.end_fill()
        #tường phải bênh viện
    move_pen(-105,-200)
    pen.pencolor("#61a898")
    pen.fillcolor("#61a898")
    pen.begin_fill()
    draw_hcn(65,105)
    pen.end_fill()
        #cửa sổ
    move_pen(-95,-190)
    for i in range(4):
        pen.pencolor("#dbeede")
        pen.fillcolor("#dbeede")
        pen.begin_fill()
        draw_hcn(45,13)
        pen.end_fill()
        pen.penup()
        pen.left(90)
        pen.forward(25)
        pen.pendown()
        pen.right(90)
        pen.penup()
        #nóc
    move_pen(-110,-95)
    pen.pencolor("#407b7a")
    pen.fillcolor("#407b7a")
    pen.begin_fill()
    draw_hcn(75,10)
    pen.end_fill()

        #tường giữa
    move_pen(-215,-200)
    pen.pencolor("#8cd4c3")
    pen.fillcolor("#8cd4c3")
    pen.begin_fill()
    draw_hcn(110,155)
    pen.end_fill()
        #cửa chính
    move_pen(-170,-200)
    pen.pencolor("#dbeedf")
    pen.fillcolor("#dbeedf")
    pen.begin_fill()
    draw_hcn(25,35)
    pen.end_fill()
    pen.forward(12)
    pen.left(90)
    pen.pencolor("#417b7a")
    pen.forward(35)
    pen.right(90)
        #cửa sổ
    y = -150
    move_pen(-205, y)
    for i in range(3):
        for j in range(4):
            pen.pencolor("#dceede")
            pen.fillcolor("#dceede")
            pen.begin_fill()
            draw_hcn(15,25)
            pen.end_fill()
            pen.penup()
            pen.forward(25)
            pen.pendown()
        pen.penup()
        pen.goto(-205,y+35)
        y+=35
        #nóc
    move_pen(-225,-45)
    pen.pencolor("#417b7a")
    pen.fillcolor("#417b7a")
    pen.begin_fill()
    draw_hcn(130,10)
    pen.end_fill()
        #logo chữ thập
    move_pen(-160,-50)
    pen.pencolor("#fe4c5f")
    pen.fillcolor("#fe4c5f")
    pen.begin_fill()
    pen.circle(13)
    pen.end_fill()

    move_pen(-162,-45)
    pen.pencolor("#fffcfd")
    pen.fillcolor("#fffcfd")
    pen.begin_fill()
    draw_hcn(5,15)
    pen.end_fill()
    move_pen(-167,-40)
    pen.pencolor("#fffcfd")
    pen.fillcolor("#fffcfd")
    pen.begin_fill()
    draw_hcn(15,5)
    pen.end_fill()


    #nhà đen nhỏ bên cạnh
    move_pen(-365,-200)
    pen.pencolor("#4d5b66")
    pen.fillcolor("#4d5b66")
    pen.begin_fill()
    draw_hcn(25,125)
    pen.end_fill()

            #cửa sổ
    move_pen(-355,-192)
    for i in range(5):
        pen.pencolor("#cee1e7")
        pen.fillcolor("#cee1e7")
        pen.begin_fill()
        draw_hcn(5,15)
        pen.end_fill()
        pen.penup()
        pen.left(90)
        pen.forward(22)
        pen.right(90)
        pen.pendown()

    #nhà vàng nhỏ bên cạnh
    move_pen(-340,-200)
    pen.pencolor("#f7be65")
    pen.fillcolor("#f7be65")
    pen.begin_fill()
    draw_hcn(20,95)
    pen.end_fill()
            #cửa sổ
    move_pen(-335,-190)
    for i in range(5):
        pen.pencolor("#cee1e7")
        pen.fillcolor("#cee1e7")
        pen.begin_fill()
        draw_hcn(6,6)
        pen.end_fill()
        pen.penup()
        pen.left(90)
        pen.forward(15)
        pen.right(90)
        pen.pendown()


    #Cây
    move_pen(-410,-200)
    draw_tree_elip(15,50)

    move_pen(-440,-200)
    draw_tree_circle(12,90,40)

    move_pen(-510,-200)
    draw_tree_elip(20,90)

    move_pen(-550,-200)
    draw_tree_circle(10,50,40)

    move_pen(420,-200)
    draw_tree_circle(10,50,40)

    move_pen(450,-200)
    draw_tree_elip(10,50)

    move_pen(490,-200)
    draw_tree_elip(12,80)

    move_pen(550,-200)
    draw_tree_circle(10,60,40)


    #vẽ nền đường
        #mặt đường
    move_pen(-900, -400)
    pen.pencolor("#4d4d4d")
    pen.pensize(2)
    pen.fillcolor("#4d4d4d")
    pen.begin_fill()
    draw_hcn(1800,200)
    pen.end_fill()
        #lề đường
    move_pen(-900,-210)
    pen.pencolor("#89999a")
    pen.pensize(25)
    pen.forward(1800)
        #vạch kẻ đường trắng
    move_pen(-880, -260)
    pen.pencolor("#f6f6f6")
    pen.pensize(5)
    for i in range(2):
        for i in range(20):
            pen.forward(80)
            pen.penup()
            pen.forward(20)
            pen.pendown()
        move_pen(-880, -340)
        #vạch kẻ đường vàng
    move_pen(-900, -300)
    pen.pencolor("#ffc93e")
    pen.forward(1800)


    turtle.done()

else: 
    print("Lựa chọn không hợp lệ, vui lòng thử lại!")