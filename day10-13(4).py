리스트 = list("나가나다라사아자하카타")
print(리스트)
반환값1 = 리스트.pop(6)
print(리스트)
반환값2 = 리스트.pop()
print(리스트)
print('반환값:', 반환값1, 반환값2)
리스트.append('나')
print(리스트)
del 리스트[5]
print(리스트)
리스트.remove("나")
print(리스트)
리스트.insert(1, '1')
print(리스트)
리스트.remove('1')
print(리스트)
리스트.sort()
print("정렬후:", 리스트)

# leambda를 사용한 sorting 방법
리스트2 = ['a',1,8,3,4,'b','ㅏ','ㅁ',' ']

리스트2.sort(key= lambda 리스트1: str(리스트1))

print(리스트2)