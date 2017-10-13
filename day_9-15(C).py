import turtle

X = turtle.Turtle()

while True:
    x = turtle.textinput("문자 입력", "l,r,q 나 enter를 누르십시요")

    if x == 'l':
        X.left(90)
        X.forward(100)
    elif x == 'r':
        X.right(90)
        X.forward(100)
    elif x == 'q':
        X.forward(100)
    elif x == '':
        break
    else:
        print("다시 입력하시요")
