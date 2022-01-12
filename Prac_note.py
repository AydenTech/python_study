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

## 답안
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

## for 문
family = ['mother', 'father', 'gentleman', 'sexy lady']
for x in family:        # family의 각 항목 x에 대하여:
    print(x, len(x))    # x와 x의 길이를 출력하라.

a = [4, 5, 6, 7]
for i in a:
    if i <= 5:
        print(i)
