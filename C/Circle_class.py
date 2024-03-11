import turtle
import math
pen = turtle.Turtle()
pen.penup()

class Circle :
    r = 0
    x = 0
    y = 0

    def __init__(self,ts_r,ts_x,ts_y) :
        self.r = ts_r
        self.x = ts_x
        self.y = ts_y

    def draw_circle(self):
        pen.goto(self.x,self.y)
        pen.pendown()
        pen.circle(self.r)
        turtle.done()
    
    def perimeter(self): 
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

c = Circle(100, -200, 0)
c.draw_circle()
print("C = ", c.perimeter())
print("S = ", c.area())