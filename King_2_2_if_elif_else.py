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


