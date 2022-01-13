## for 문
family = ['mother', 'father', 'gentleman', 'sexy lady']
for x in family:        # family의 각 항목 x에 대하여:
    print(x, len(x))    # x와 x의 길이를 출력하라.

## practice
a = [4, 5, 6, 7]
for i in a:
    print(i)
## same
b = range(4,8)
for j in b:
    print(j)

## 예제) 정수 입력 받아 그 수를 그 수만큼 반복해서 출력
c = int(input('정수를 입력하세요: '))
for d in range(c):
    print('', c)

# for ab in range(3):
#     print(3)

## 예제) 정수 입력받아 1부터 그 수까지와 제곱수를 출력 for 활용
x = int(input('put any integer: '))
for i in range(1, x + 1):
    print(i, i * i)

## 예제) 온도 범위 입력받고 그 외는 경고 및 종료, 범위 내면 계속, -999면 종료
minmax = input('min max 를 입력: ').split() #.split() 을 이용하여 연속된 문자를 나눌 수 있음
print(minmax)
min = int(minmax[0])
max = int(minmax[1])

temp = int(input('temperature: '))

while temp != -999:
    if min <= temp <= max:
        print('nothing to report')
        temp = int(input('temperature: '))
    else:
        print('Alert!!!')
        break
