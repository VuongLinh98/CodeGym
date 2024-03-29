from turtle import*
hideturtle()
speed(0)
def moon(x, y, size, col_fill, col_bg):
    penup()
    goto(x, y)
    pencolor(col_fill)
    fillcolor(col_fill)
    begin_fill()
    circle(size)
    end_fill()
    penup()
    goto(x + size * 0.45, y + size * 0.35)
    pencolor(col_bg)
    fillcolor(col_bg)
    begin_fill()
    circle(size)
    end_fill()
    penup()
moon(300, 100, 120, '#F9F400', '#000000')
done()