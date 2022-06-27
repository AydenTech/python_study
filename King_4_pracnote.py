# palindrome
# s = input('input: ')
#
# def palindrome(s):
#     s = s.lower()
#     s = s.replace(' ', '')
#     return s[:] == s[::-1]
#
#
# print(palindrome(s))


# t = "hello Python!"
# t.find('P')
# print(t.find('P'))
# h = t[0:6]
# print(h)
#
# h.rstrip() #공백제거
# print(h)
#
# print(t.split())
#
# prime = [3, 7, 11]
# print(prime)
# prime.append(5)
# print(prime)
#
# prime.sort()
# print(prime)
#
# prime.insert(1, 2)
# print(prime)
#
# del prime[4]
# print(prime)
#
# print(' ')
# a = prime.pop()
# print(prime)
# print(a)
#
# prime[0] = 1
# print(prime)


# characters = []
# sentence = 'Be happy!'
# for char in sentence:
#     characters.append(char)
#
# print(characters)
#
# print(list('Be happy!'))
#
# my_int = 123
# print(type(my_int))
# print(my_int)
#
# print(' ')
# str(my_int)
# print(type(str((my_int))))
#
# print(' ')
# print(my_int)
# print(str(my_int))
#
# my_str = str(my_int)


# a = int('123')
# b = float('123')
# print(a, b)
#
# one_to_ten = list(range(1, 11))
# print(one_to_ten)
#
# print(sum(one_to_ten))


## 총점, 평균점수 구하기!
# a = [90, 85, 70]
# b = [88, 79, 92]
# c = [100, 100, 100]
# d = [90, 60, 70]
# students = [a, b, c, d]
#
# for scores in students:
#     tot = 0
#     for points in scores:
#         tot = tot + points
#     average = tot / 3
#     print(scores, tot, average)


## Practice 각자리의 숫자 합 함수 만들기
# num = int(input('any integer: '))
#
# def sum_of_digits(num):
#     sum = 0
#     for d in list(str(num)):
#         sum += int(d)
#
#     return sum
#
# print(sum_of_digits(num))


## 줄기 잎 그림
# score = [0, 0, 2, 4, 7, 9]
# score += [11, 21, 11, 13, 18]
# score += [20]
# print(score)
# score.sort()
# print(score)
#
# stem_leaf = [[], [], []]
#
# for i in score:
#     d, m = divmod(i, 10)
#     stem_leaf[d].append(m)
#
# print(stem_leaf)
#
# for x in range(len(stem_leaf)):
#     print(f'{x}: {stem_leaf[x]}')


## map() 함수 이용해서 sumOfDigjts 작성
# num = int(input('any input: '))
#
# def sum_of_digits(num):
#     digits = map(int, list(str(num)))
#     return sum(digits)
#
# if __name__ == '__main__': #이거 뭐더라...
#     print(sum_of_digits(num))


# a = [1.2, 5, 8.2, 4.4]
# print(len(a))
#
# for i in range(len(a)):
#     a[i] = int(a[i])
#
# print(a)


# a = [1.2, 5, 8.2, 4.4]
# a = list(map(int, a))
# print(a)


## sum of digits
# a = int(input('put any integer: '))
#
# def sumofdigit(a):
#     b = map(int, list(str(a)))
#     return sum(b)
#
# print(sumofdigit(a))

## 30 미만의 소수 구하기
# def prime(n):
#     L = list(range(2, n + 1))
#     L2 = L[:] # https://stackoverflow.com/a/10665602
#
#     for p in L:
#         for q in L:
#             if (q in L2) and (q != p and q % p == 0):
#                 L2.remove(q)
#
#     print(L2)
#
# if __name__ == '__main__':
#     prime(int(input()))

# def digitsum(num):
#     sum = 0
#     a = str(num)
#     b = list(a)
#     for i in b:
#         sum += int(i)
#
#     return sum
#
# print(digitsum(11))


## Again, getting a prime
# def primef(n):
#     L = list(range(2, n+1))
#     L2 = L
#     for p in L:
#         for q in L:
#             if (q in L2) and (q != p and q % p == 0):
#                 L2.remove(q)
#
#     print(L2)
#
# if __name__=='__main__':
#     primef(int(input('any integer: ')))


a = int(input())
b = 0
c = []

while True:
    a, b = divmod(a, 2)
    c.insert(0, b)
    if a == 0:
        break

print(c)