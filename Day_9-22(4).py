import turtle

창 = turtle.Screen()
펜 = turtle.Pen()

def 글씨쓰기(x, y):
    펜.pu()
    펜.goto(x, y)
    펜.pd()

    for i in range(4):
        펜.fd(20)
        펜.left(90)

창.onclick(글씨쓰기)
창.mainloop()