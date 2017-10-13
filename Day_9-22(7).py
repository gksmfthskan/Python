import turtle

펜 = turtle.Pen()

def 직사각형(X , Y, 선두께 = 1, 선색깔 = 'red'):
    펜.pensize(선두께)
    펜.color(선색깔)

    for i in range(2):
        펜.fd(X)
        펜.left(90)
        펜.fd(Y)
        펜.left(90)

펜.penup()
펜.goto(-300,-300)
펜.pendown()
직사각형(100,150)
직사각형(200,250,4)
직사각형(300,350,1,'blue')
직사각형(400,450,3,'yellow')

turtle.mainloop()