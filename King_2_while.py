## 2.1 While 반복문
import sys

num = 1
while num <= 100:
    print(num)
    num += + 1  # num = num + 1 과 같은 의미

## 연습문제) 정수를 입력받아 그 정수를 그 값 만큼 반복해서 출력하세요(입력과 출력을 한 줄 띄어 구분하세요)
a = int(input('정수를 입력하세요: '))
print( )
num = 1
while num <= a:
    print(a)
    num = num + 1

## 연습문제) 정수를 입력받아 1부터 입력된 정수까지 정수와 제곱수를 프린트하시오(예: 2-> 1, 1; 2, 4)
b = int(input('정수를 입력하세요: '))
print( )
i = 1
while i <= b:
    print(i, i**2)
    i += 1

## etc
c = 3.451957689922303
print(round(c, 4)) #round(a, n): n째자리까지 반올림
# round 연습문제) 공을 100m 에서 떨어뜨림. 튕길 때마다 2/3 높이로 튀어오름. 10번 튕길동안 높이를 소수점 네자리까지 출력하시오.
height = 100
i = 1
while i <= 10:
    i = i+1
    height = height * 2/3
    print(round(height, 4))