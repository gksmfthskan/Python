import turtle
x = [1, 'a', "안녕", 3.4]

print(type(x))

print(x[0])

x[0] = 1.5

print(x[0])

print(len(x))

angela = turtle.Turtle()
for color_ in ["yellow", "red", "purple", "blue"]:

    angela.color(color_) # 거북이 펜색깔 변경
    angela.forward(100) # 들여쓰기로 for 구역 선언
    angela.left(90)

turtle.mainloop()