# chap 3.5
# Lambda 매개변수: 표현식
# (lambda 변수: 표현식)()
def hap(x, y):
    return x + y


print(hap(10, 30))


# 이를 lambda 를 이용하여 표현
(lambda x, y: x + y)(10, 30)
print((lambda x, y: x + y)(10, 30))


# map()
# map(함수, 리스트)
A = map(lambda x: x ** 2, range(6))
print(list(A))

x=2
y=3
# reduce()
# reduce(함수, 시퀀스)
# 시퀀스 = 문자열, 리스트, 튜플 과 같은 것들
# 시퀀스의 원소들을 함수에 누적해서 적용시킴

from functools import reduce
# 파이썬3 에서는 써줘야함
# B = reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
# print(B)

C = reduce(hap, list(range(5)))
print(C)