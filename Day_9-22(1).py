import turtle

pen = turtle.Pen()

def 직사각형(X, Y):
    for _ in range(2):
        pen.fd(X)
        pen.left(90)
        pen.fd(Y)
        pen.left(90)

직사각형(300, 200)
직사각형(100,100)

turtle.mainloop()