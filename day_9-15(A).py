import turtle

angela = turtle.Turtle() # angela 거북이 만들기

r = 100 # 반지름 100인 원
n = 20 # n개의 발자국

angela.shape('turtle') # 거북이 모양
angela.penup() # 선을 그리지 않는다.
angela.sety(-r) # 처음 시작하는 y 좌표를 -r로 설정

for i in range(n): # n번 반복
    angela.stamp() # 발자국 찍기
    angela.circle(r, 360 / n) # 반지름 r인 원 위에서 360/n도 회전
turtle.mainloop()