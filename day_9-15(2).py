import turtle

jisoo = turtle.Turtle() # jisoo 거북이 만들기
jisoo.shape('turtle') # 거북이 모양 변경
jisoo.color("white")
jisoo.pensize(3)

x = turtle.numinput("좌, 우회전", "숫자를 입력하시오:") # 팝업창을 이용하여 숫자를 입력받는다.

if x > 0:
    jisoo.color("red")
    jisoo.left(90) # 양수이면 왼쪽으로 회전
else:
    jisoo.color("blue")
    jisoo.right(90) # 양수가 아니면 오른쪽으로 회전


jisoo.forward(100) # 100만큼 거북이 움직이기


turtle.mainloop()