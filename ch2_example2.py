wen = 3
nigth = 137
num = (wen+nigth)%7

if num==0:
    print("오늘은 일요일 입니다.")
elif num==1:
    print("오늘은 월요일 입니다.")
elif num==2:
    print("오늘은 화요일 입니다.")
elif num==3:
    print("오늘은 수요일 입니다.")
elif num==4:
    print("오늘은 목요일 입니다.")
elif num==5:
    print("오늘은 금요일 입니다.")
else:
    print("오늘은 토요일 입니다.")
