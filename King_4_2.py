x = 'banana'
print(x[0])
print(x[:3])
print(x[3:])

x = 'n' + x[1:]
print(x)

s = "Hello Python!"
s.find('P')
print(s.find('P'))

h = s[:6]  #Hello 뒤에 한칸 ' '있음
print(h)
h.rstrip()  #Hello 뒤에 한칸 ' '없앰
print(h)

s.split()
print(s.split())  # 공백에서 분할 -> 리스트로 생성
print(s.split()[1])


# LIST
prime = [3, 7, 11]
prime.append(5)  # prime 리스트에 5를 추가
print(prime)

prime.sort()  # prime을 원소 크기 순 정렬
print(prime)

prime.insert(0, 2)  # prime 리스트의 [0] 번에 2 를 삽입
print(prime)

del prime[4]  # prime [4]번 원소 11 삭제
print(prime)

a = prime.pop()  # pop 은 원소를 삭제하고 반환(return)함
print(prime)  # 마지막 원소가 삭제되어 [2, 3, 5] 만 남고 a = 7 이됨
print(a)

prime[0] = 1  # 원소에 새로운 값 지정
print(prime)


print(' ')  #구분용

# LISI 에 LIST 넣기 (예제 - 피자가게 주문)
orders = ['potato', ['pizza', 'coke', 'salad'], 'hamburger']
print(orders[1])
print(orders[1][2])  # orders[1] 의 [2]번 원소 'salad'


print(' ') #구분용 ㅋ

# 행렬
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

characters = []
sentence = 'Be happy!'
for char in sentence:
    characters.append(char)  # sentence 안의 모든 문자를 characters 라는 리스트에 삽입

print(characters)

# 위 과정은 그냥 list() 함수를 통해 할 수 있음
list('Be happy!')
print(list('Be happy!'))


print(' ')

# 숫자를 문자열로 바꾸기
my_int = 123
type(my_int)
print(type(my_int))

str(my_int)  #문자열 123 으로 바꿈
print(type(str(my_int)))

my_str = str(my_int)  # 이렇게 얻은 문자열을 변수에 할당

print(' ')


# 문자열을 숫자로 바꾸기
one_to_ten = list(range(1,11))
print(one_to_ten)

sum(one_to_ten)  # 원소들의 합 계산
print(sum(one_to_ten))

print(' ')


# 예제) 성적표
chulsu = [90, 85, 70]
younghee = [88, 79, 92]
yong = [100, 100, 100]
minsu = [90, 60, 70]

students = [chulsu, younghee, yong, minsu]

for scores in students:
    print(scores)

for scores in students:
    total = 0
    for p in scores:
        total = total + p
    average = total / 3
    print(scores, total, average)


print(' ')


# 예제) 세자리 숫자 입력받아 digit 의 합 계산하는 함수 정의
def sumOfDigits(num):
    sum = 0
    for r in list(str(num)):
        sum += int(r)

    return sum

if __name__=='__main__':
    print(sumOfDigits(47253))
    print(sumOfDigits(643))


print(' ')


# 예제) 줄기와 잎 그림
score = [0, 0, 2, 4, 7, 9]
score += [11, 11, 13, 18]
score += [20]
print(score)

stem_leaf = [[], [], []]

for j in score:
    d, m = divmod(j, 10)  # j 를 10 으로 나눈 몫 나머지
    stem_leaf[d].append(m)  # 몫이 0,1,2가 나올텐데 암튼 그럼 0,1,2번째 원소List에 나머지(m)를 삽입

print(stem_leaf)

for k in range(len(stem_leaf)):  # stem_leaf 크기가 3이니깐 k 는 0, 1, 2 가 됨
    print(f'{k}: {stem_leaf[k]}')

