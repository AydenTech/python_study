## 파이썬 인터프리터
import sys

print('직각삼각형 그리기\n')
leg = int(input('변의 길이: '))

for i in range(leg):
    print('* ' * (i + 1))  # str * int

area = (leg ** 2) / 2
print('넓이:', area)
