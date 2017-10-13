import turtle

jisoo = turtle.Turtle() # jisoo 거북이 만들기
jisoo.shape('turtle') # 거북이 모양 변경
jisoo.pensize(3)

x = turtle.numinput("0부터 90까지", "숫자를 입력하시오:")
if  x <= 30:
    jisoo.color("red")
    jisoo.left(30) # 양수이면 왼쪽으로 회전
elif x <= 60:
    jisoo.color("blue")
    jisoo.left(60) # 양수가 아니면 오른쪽으로 회전
else:
    jisoo.left(90)


jisoo.forward(100) # 100만큼 거북이 움직이기


turtle.mainloop()