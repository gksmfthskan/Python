import turtle
import random
import math

창 = turtle.Screen() # 거북이 창

우주선 = turtle.Pen() # 게이머
우주선.color('blue')
우주선.shape('turtle')
우주선.penup()
우주선.speed(0)
소행성1 = turtle.Pen() # 소행성1
소행성1.color('red')
소행성1.shape('circle')
소행성1.penup()
소행성1.speed(0)
소행성1.goto(random.randint(-300, 0), random.randint(-300, 300))

소행성2 = turtle.Pen() # 소행성2
소행성2.color('red')
소행성2.shape('circle')
소행성2.penup()
소행성2.speed(0)
소행성2.goto(random.randint(-300, 0), random.randint(-300, 300))

def 왼쪽():
    우주선.goto(우주선.pos() + (-10, 0))

def 오른쪽():
    우주선.goto(우주선.pos() + (10, 0))

def 위():
    우주선.goto(우주선.pos() + (0, 10))

def 아래():
    우주선.goto(우주선.pos() + (0, -10))

창.onkeypress(왼쪽, "Left")
창.onkeypress(오른쪽, "Right")
창.onkeypress(위, "Up")
창.onkeypress(아래, "Down")
창.listen()

def 놀자():
    소행성1.forward(2)
    소행성2.forward(2)
    창.ontimer(놀자, 100)
창.ontimer(놀자, 100)

창.mainloop()