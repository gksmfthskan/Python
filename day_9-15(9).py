import random
import turtle

rdg = random.Random() # 임의의 수를 만들 객체 만들기

jisoo = turtle.Turtle() # jisoo 거북이 만들기

for _ in range(60):
    jisoo.forward(30) # 50만큼 거북이 움직이기

    x = rdg.randint(-1, 1) # -1보다 크거나 같고 1보다 작거나 같은 임의의 정수
    if x > 0:
        jisoo.left(90) # 양수이면 왼쪽으로 회전
    elif x == 0:
        jisoo.forward(90) # 양수가 아니면 오른쪽으로 회전
    else:
        jisoo.right(90)

turtle.mainloop()