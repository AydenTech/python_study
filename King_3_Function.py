a = 3
for i in range(1, 10):
    print(a, '*', i, '=', a * i)

b = 4
for i in range(1, 10):
    print(f'{b} * {i} = {b * i}')


##구구단 출력하기
def googoo(m):
    for i in range(1, 10):
        print(f'{m} * {i} = {m * i}')


m = int(input('integer: '))
googoo(m)

## 삼각형 넓이 구하기 return 활용 (함수)

width = int(input('밑변: '))
height = int(input('높이: '))

print(f'밑변: {width}, 높이: {height}')


def tri_area(width, height):
    y = (1 / 2) * width * height
    # print(y)
    return y


ret = tri_area(width, height)
print(ret)


## 퀴즈 만들기
def quiz():
    ans = input('1 + 2 = ')
    return 1 + 2 == int(ans)


print(quiz())


## Korean_number 정의하기 함수

def Korean_num(v):
    if v == 1:
        return '일'
    elif v == 2:
        return '이'
    elif v == 3:
        return '삼'


v = int(input("num 1~3: "))
print(Korean_num(v))

## 나이 계산
from datetime import datetime
today = datetime.today()
today
print(today)
print(today.year)
x = int(input('your birth year: '))


def age_fn(x):
    return today.year - x


print('your age is...')
print(age_fn(x))



## 단리 구하기 함수
def simple_interest(p, r, t):
    return p * r * t

p = float(input('원금: '))
r = float(input('이율: '))
t = float(input('시간: '))
print(simple_interest(p, r, t))

## 원금 + 이자
def simple_interest_amount(p, r, t):
    return p + p*r*t
p = float(input('원금: '))
r = float(input('이율: '))
t = float(input('시간: '))
print(simple_interest_amount(p, r, t))

## 복리 원리금
def compound_interest_amount(p, r, t, n):
    return p*(1+r/n)**(n*t)
p = float(input('원금: '))
r = float(input('이율: '))
t = float(input('몇년간?: '))
n = float(input('연 몇번 적용?: '))
print(compound_interest_amount(p, r, t, n))

## 지역변수 전역변수
def e_is_10():
    global e  # 전역변수
    e = 10
    print('e 값은 ', e, '입니다')
    return e

print(e_is_10())
print(e)


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
print(list(filter(lambda x: x<5, range(10))))

## 2로 나눈 나머지가 0 -> 0=False 니까 버려짐 1=True 는 남겨짐
filter(lambda x: x % 2, range(10))
list(filter(lambda x: x % 2, range(10)))
print(list(filter(lambda x: x % 2, range(10))))
## 따라서 이 함수에서 남는 것은 홀수들 [1,3,5,7,9]


