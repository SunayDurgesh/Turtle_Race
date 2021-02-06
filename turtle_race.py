from random import randint
from turtle import *
import time


penup()
goto(-140,140)

for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

    
t1.color('pink')
t1.shape('turtle')


t2.color('blue')
t2.shape('arrow')


t3.color('green')
t3.shape('triangle')

t4.color('orange')
t4.shape('classic')

t1.penup()
t1.goto(-160,100)
t1.pendown
for turn in range(10):
    t1.right(36)


t2.penup()
t2.goto(-160,70)
t2.pendown
for turn in range(72):
    t2.left(5)

t3.penup()
t3.goto(-160,40)
t3.pendown
for turn in range(60):
    t3.right(6)


t4.penup()
t4.goto(-160,10)
t4.pendown
for turn in range(30):
    t1.left(12)

for turn in range(100):
    t1.forward(randint(1,5))
    t2.forward(randint(1,5))
    t3.forward(randint(1,5))
    t4.forward(randint(1,5))

    


    
    








