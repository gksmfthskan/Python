import turtle

jisoo = turtle.Turtle() # jisoo 거북이 만들기
jisoo.shape('turtle') # 거북이 모양 변경
jisoo.pensize(3)

x = turtle.numinput("좌, 우회전", "숫자를 입력하시오:") # 팝업창을 이용하여 숫자를 입력받는다.

if x > 0:
    jisoo.color("red")
    jisoo.left(90)
elif x < 0:
    jisoo.color("blue")
    jisoo.right(90)

jisoo.forward(100)


turtle.mainloop()