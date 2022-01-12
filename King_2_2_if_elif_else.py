## 조건문
import sys

a = 1234 * 4
b = 123456 / 2

if a > b:
    print('a')
else:
    print('b')

## more
c = 15 * 5
d = 15 + 15 + 15 + 15 + 15
if c > d:
    print('c is greater than d')
elif c == d:
    print('c is equal to d')
elif c < d:
    print('c is smaller than d')
else:
    print('I don\'t know')

## if 문
x = 48
y = 4
if x % y == 0:
    print(f'{x} can be divided by {y}')
elif x % y != 0:
    print(f'{x} cannot be divided by {y}')

## break : 조건문 종료
max = 10

while True:
    num = int(input())
    if num > max:
        print(num, 'is too big!')
        break

## 연습문제
number = int(input('input integer: '))
if number == 1:
    print('one')
elif number == 2:
    print('two')
elif number ==3:
    print('three')

## 연습문제 input()으로 사용자로부터 입력받은 정수를 계속 더해나가다가, 음수가 입력되면 중단하고 그 전까지 계산한 값을 출력하는 파이썬 스크립트를 작성하세요.
e = 0
while True:
    f = int(input('any integer: '))
    if f <= 0:
        break
    else:
        e = e + f
        print(e)

## 연습문제) 윤년 구하기

while True:
    result = None
    year = int(input('년도를 입력하세요: '))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
            else:
                result = False
        else:
            result = True
    else:
        result = False
    if result: # if result == True: 로 적어도 무방하나 while True: 로 시작했기 때문에 지금과 같이 적는 것이 나음
        print(f'{year} is leap year')
    else:
        print(f'{year} is not leap year')