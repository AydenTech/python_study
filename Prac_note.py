# a = 0
# while True:
#     f = int(input('any number: '))
#     if f < 0:
#         break
#     else:
#         a += f
#         print(a)
#
# ## 윤년 구하기 연습
# ## 4로 나누어 떨어지지 X 윤년 X
# ## 연도가 100으로 나누어 떨어지지 X 윤년 O
# ## 연도가 400으로 나누어 떨어지지 X 윤년 X
#
# x = int(input('년도를 입력하세요: '))
# if x % 4 != 0:
#     print(f'{x}년은 윤년이 아닙니다')
# elif x % 100 != 0:
#     print(f'{x}년은 윤년입니다')
# elif x % 400 != 0:
#     print(f'{x}년은 윤년이 아닙니다')
# else:
#     print(f'{x}년은 윤년입니다')
#
# # 답안
# while True:
#     is_leap_year = None
#
#     year = int(input())
#
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 is_leap_year = True
#             else:
#                 is_leap_year = False
#         else:
#             is_leap_year = True
#     else:
#         is_leap_year = False
#
#     if is_leap_year:
#         print(f'{year} is a leap year')
#     else:
#         print(f'{year} is not a leap year')
#
# ## for 문
# family = ['mother', 'father', 'gentleman', 'sexy lady']
# for x in family:        # family의 각 항목 x에 대하여:
#     print(x, len(x))    # x와 x의 길이를 출력하라.
#
# a = [4, 5, 6, 7]
# for i in a:
#     if i <= 5:
#         print(i)
#
# for ab in range(3):
#     print(3)
#
# ## 예제) 정수 입력받아 1부터 그 수까지와 제곱수를 출력 for 활용
# x = int(input('put any integer: '))
# for i in range(1, x + 1):
#     print(i, i * i)
#
# minmax = input('min max 를 입력: ').split() #.split() 을 이용하여 연속된 문자를 나눌 수 있음
# print(minmax)
# min = int(minmax[0])
# max = int(minmax[1])
#
# temp = int(input('temperature: '))
#
# while temp != -999:
#     if min <= temp <= max:
#         print('nothing to report')
#         temp = int(input('temperature: '))
#     else:
#         print('Alert!!!')
#         break
#
# def printer_Lee():
#     print('I am Haram Lee')
#
# printer_Lee()
#
# # 삼각형 넓이 구하기 return 활용 (함수)
#
# width = int(input('밑변: '))
# height = int(input('높이: '))
#
# print(f'밑변: {width}, 높이: {height}')
#
#
# def tri_area(width, height):
#     y = (1 / 2) * width * height
#     # print(y)
#     return y
#
#
# ret = tri_area(width, height)
# print(ret)
#
# ## 퀴즈 만들기
# def quiz():
#     ans = input('1 + 2 = ')
#     return 1 + 2 == int(ans)
#
#
# print(quiz())
#
# # Korean_number 정의하기 함수
#
# def Korean_num(v):
#     if v == 1:
#        return '일'
#     elif v == 2:
#        return '이'
#     elif v == 3:
#         return '삼'
#
# a = int(input("num 1~3: "))
# print(Korean_num(a))
#
# from datetime import datetime
# today = datetime.today()
# today
# print(today)
# print(today.year)
# x = int(input('your birth year: '))
#
#
# def age_fn(x):
#     return today.year - x
#
#
# print('your age is...')
# print(age_fn(x))
#
# ## 단리 구하기 함수
#
#
# def simple_interest(p, r, t):
#     return p * r * t
#
#
# p = float(input('원금: '))
# r = float(input('이율: '))
# t = float(input('시간: '))
# print(simple_interest(p, r, t))
#
#
# def simple_interest_amount(p, r, t):
#     return p + p*r*t
# p = float(input('원금: '))
# r = float(input('이율: '))
# t = float(input('시간: '))
# print(simple_interest_amount(p, r, t))

## 복리 원리금
# def compound_interest_amount(p, r, t, n):
#     return p*(1+r/n)**(n*t)
# p = float(input('원금: '))
# r = float(input('이율: '))
# t = float(input('몇년간?: '))
# n = float(input('연 몇번 적용?: '))
# print(compound_interest_amount(p, r, t, n))

# ## 지역변수 전역변수
# def e_is_10():
#     global e  # 전역변수
#     e = 10
#     print('e 값은 ', e, '입니다')
#     return e
#
# print(e_is_10())
# print(e)

# ## 매개변수
# def hap(x, y):
#     return x+y
# print(hap(3, 4))

# (lambda x,y: x+y)(10,20)
# print((lambda x,y: x+y)(10,20))

# map(lambda x: x ** 2, range(5))
# list(map(lambda x: x ** 2, range(5)))

## reduce(함수, 시퀀스)
# from functools import reduce
# reduce(lambda x, y: x + y, [0,1,2,3,4])
# print(reduce(lambda x, y: x + y, [0,1,2,3,4]))
#
# from functools import reduce
# reduce(lambda x, y: y+x, 'abcde')
# print(reduce(lambda x, y: y+x, 'abcde'))

## filter(lambda x: x<5, range(10))
# print(list(filter(lambda x: x<5, range(10))))
# filter(lambda x: x % 2, range(10))
# list(filter(lambda x: x % 2, range(10)))
# print(list(filter(lambda x: x % 2, range(10))))

# temp_range = input('put min and max temp:').split()
# print(temp_range)
# min_temp = int(temp_range[0])
# max_temp = int(temp_range[1])
# temp = int(input('temp?'))
# while temp != 999:
#     if min_temp <= temp <= max_temp:
#         print(f'{temp} is good')
#         temp = int(input('next temp: '))
#     else:
#         print(f'{temp} is out of range!!!')
#         break

## 음수가 입력되면 중단하고 그 전까지 계산한 값을 출력하는 파이썬 스크립트를 작성하세요.

# num = 0
# while True:
#     a = int(input('integer: '))
#     if a >= 0:
#         num = num + a
#         print(num)
#     else:
#         break

# 구구단
# a = int(input('몇단?: '))
# def gugu(m):
#     if m <= 9:
#         for i in range(1, 10):
#             print(f'{m} * {i} = {m * i}')
#     else:
#         for j in range(1, m+1):
#             print(f'{m} * {j} = {m * j}')
#
# gugu(a)

# def TF_Quiz():
#     ans1 = input('2+3= ')
#     return 2+3 == int(ans1)
#
# print(TF_Quiz())


# # 나이구하기
# from datetime import datetime
# today = datetime.today()
#
# print(today)
# print(today.year)
# x = int(input('your birth year: '))
#
# def age_fn(x):
#     return today.year - x + 1
#
# print('your age is...')
# print(age_fn(x))


# # 지역변수 전역변수
# def e_is_10():
#     global e  # 전역변수
#     e = 10
#     print('e 값은 ', e, '입니다')
#     return e
#
# print(e_is_10())
# print(e)  #함수안에 있지 않지만 전역변수라 10으로 들어옴


# ## 매개변수
# def hap(x, y):
#     return x+y
# print(hap(3, 4))
#
# (lambda x,y: x+y)(10,20)
# print((lambda x,y: x+y)(10,20))
#
# map(lambda x: x ** 2, range(5))
# list(map(lambda x: x ** 2, range(5)))
#
# print(map(lambda x: x ** 2, range(5)))
# print(list(map(lambda x: x ** 2, range(5))))


# reduce(함수, 시퀀스)
from functools import reduce
reduce(lambda x, y: x + y, [0,1,2,3,4])
print(reduce(lambda x, y: x + y, [0,1,2,3,4]))

from functools import reduce
reduce(lambda x, y: y+x, 'abcde')
print(reduce(lambda x, y: y+x, 'abcde'))
