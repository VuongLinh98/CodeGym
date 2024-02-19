import turtle
import random

random_col = ["red", "blue", "green", "white", "black", "yellow", "pink", "brown"]

t = turtle.Turtle()
t.pensize(3)
t.speed(20)
t.pencolor(random.choice(random_col))

elip = 1
while True :  
    for i in range(2) :
        t.circle(100,90)
        t.circle(50,90)
    t.right(10)
    t.pencolor(random.choice(random_col))
    elip += 1
    if elip >= 50 :
        break

turtle.done()