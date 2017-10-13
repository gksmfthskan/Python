import turtle

pen = turtle.Pen()

def 정삼각형 (X):
    for i in range(3):
        pen.fd(X)
        pen.left(120)

정삼각형(50)
정삼각형(100)
정삼각형(150)

turtle.mainloop()