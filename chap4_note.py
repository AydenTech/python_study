def palindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
    return s[:] == s[::-1]

# 만약 여기에 아래 행을 안썼을 경우에는
# 다른 파일에서 본 파일의 함수들(tools)을 사용할 때 불필요하게 본 파일의 메인 함수를 실행해야함. 따라서 써주는 것이 편리.
if __name__ == '__main__':
    for x in ['anna', 'banana', 'Anna', 'My gym']:
        if palindrome(x):
            print(f"'{x}' is a panlindrome")
        else:
            print(f"'{x}' is not a palindrome")

# def hello():
#     print("hello!!!!!!!!!!!!!!!")
#
#
# if __name__ == "__main__":  # __name__ == "chap4_note.py"
#     hello()
