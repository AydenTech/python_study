## 왕초보파이썬 chap1.2 변수
import sys
watch = 100000
lighter = 300
a = watch + lighter
print(a)


price = 5000
price *= 0.85
print(price)

a = 'crimson'
b = 'heart'
print(a+' '+b)

## practice problem 1.2.1
## download average speed r, time t, size rt
## if r = 800 kB/s, t = 110 s, then size = ? MB
r = 800
t = 110
s = 0.001*r*t

# 문자열 포맷팅
print(str(s) + ' MB')
# int + str
print(f'{s} MB')
# f'{변수}, 고정된문자'
print("%s MB" % s)

## 1.3 List
family = ['mom', 'dad', 'H', 'Y']
print(len(family))
print(family[2])

family.remove('H')
print(family[2])
# H가 제외되어 Y가 출력됨








