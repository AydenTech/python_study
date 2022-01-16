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
