## 데이터 타입
# 자료형
# 숫자 int float complex
# 시퀀스 문자열(str), 리스트(list), 튜플(tuple), 사용자정의시퀀스

print(type(100000000)) # 정수
print(type(2.8)) # 부동소수점수
print(type(3+4j)) # 복소수

print(type("Love your friends"))
print(type(['LOVE','YOUR','FRIENDS']))
print(type(('LOVE','YOUR','FRIENDS')))

p = 'python'
print(p[0:2])
print(p[-2:])
print(p[:])
print(p[::-1])

## 매핑
print(type(False))
## 세트: 원소순서 유지X 원소중복X 집합연산O
fruits = {'apple', 'grape', 'banaba'}
print(fruits)

print('Python'.lower())
print('Python'.replace('P', 'K'))

## 회문 판별 함수 작성 (회문: 거꾸로 읽어도 같은 단어)
x = str(input('input word: '))


def palindrome(x):

    if x[::-1] == x:
        return True
    else:
        return False

print(palindrome(x))

# def palindrome(s):
#     s = s.lower()
#     s = s.replace(' ', '')
#     return s[:] == s[::-1]
#
# if __name__ == '__main__':
#     for x in ['anna', 'banana', 'Anna', 'My gym']:
#         if palindrome(x):
#             print(f"'{x}' is a panlindrome")
#         else:
#             print(f"'{x}' is not a palindrome")

