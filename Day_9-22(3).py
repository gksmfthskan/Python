import turtle

Cir = turtle.Pen()
컬러 = ['red','blue','green','yellow']
Cir.pensize(4)

def 원그리기 (X):
    Cir.penup()
    Cir.goto(0, -X)
    Cir.pendown()
    for i in 컬러:
        Cir.pencolor(i)
        Cir.circle(X,90)


원그리기(50)
원그리기(100)
원그리기(150)
원그리기(200)

turtle.mainloop()