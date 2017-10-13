import turtle

pen = turtle.Pen()

psize = 1

def 펜_굵게():
    global psize
    pen.left(95)

    pen.pensize(psize)
    X = 50
    X = X + 30
    pen.forward(X)

for i in range(60):
    펜_굵게()