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