import turtle

X = turtle.Turtle()
X.pensize(3)

n = int(turtle.numinput("", "숫자를 입력하시오:"))
i = 0
for i in range(n):
    X.forward(70)
    X.left(360/n)

turtle.mainloop()