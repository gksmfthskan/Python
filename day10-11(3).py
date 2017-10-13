def 더하기(*숫자들):

    num = 0
    for i in 숫자들:
        num = num + i
    print(num)

인자 = range(1,1001)

더하기(*인자)
