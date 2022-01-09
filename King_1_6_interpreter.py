## 파이썬 인터프리터
import sys

print('직각삼각형 그리기\n')
leg = int(input('변의 길이: '))

for i in range(leg):
    print('* ' * (i + 1))  # str * int

area = (leg ** 2) / 2
print('넓이:', area)

## Practice problem
print('제곱 계산')
var_a = int(input('원하는 정수: '))
print(var_a ** 2)


# print("3\n")  ## \n : 엔터
# print(4)