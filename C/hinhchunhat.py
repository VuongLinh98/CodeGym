#Tính chu vi, diện tích HCN
import math
CD = float(input("Nhập giá trị Cdai: "))
CR = float(input("Nhập giá trị Crong: "))
P = (CD + CR)*2
S = CD * CR 
print("Chu vi hình chữ nhật là: " , P)
print("Diện tích hình chữ nhật là: " , S)

#vẽ hình chữ nhật
import turtle
t = turtle.Turtle()
t.fillcolor("Yellow")
t.begin_fill()
t.forward(CD)
t.right(90)
t.forward(CR)
t.right(90)
t.forward(CD)
t.right(90)
t.forward(CR)
t.end_fill()

turtle.done()
