def 리스트_합계_평균(X,Y,Z):

    국영수 = [X,Y,Z]
    합 = 0
    for i in 국영수:
        합 = 합 + i
    평 = 합/len(국영수)
    print("합계: {}".format(합))
    print("평균: {0:3.1f}".format(평))

리스트_합계_평균(90, 95, 92)
리스트_합계_평균(93, 90, 96)