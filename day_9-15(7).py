import turtle



P = turtle.Turtle()

P.pensize(3)
P.penup()
P.goto(-144,0)
P.pendown()

for i in range(5):
    P.forward(300)
    P.left(144)

turtle.mainloop()