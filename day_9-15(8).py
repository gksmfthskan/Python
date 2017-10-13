import turtle

창 = turtle.Screen()
창.bgcolor("black")

연필 = turtle.Pen()
색깔들 = ["red", "white", "blue","red", "white", "blue"]

문자열 = ["한민족", "평화", "통일","한민족", "평화", "통일"]

for x in range(1, 61):
    연필.pencolor(색깔들[x % len(문자열)])
    연필.penup()
    연필.forward(x * 5)
    연필.pendown()
    연필.write(문자열[x % len(문자열)], font=("Arial", int((x + 4) / 4), "bold"))
    연필.left(360 / len(문자열) + 5)
창.mainloop()