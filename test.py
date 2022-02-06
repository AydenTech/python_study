import chap4_note

#print("아무것도 안나옴")
chap4_note.hello()

# __name__ 에 대한 설명
# __name__ 은 작업이 이루어지고 있는 해당 파일을 지칭.
# if __name__=="__main__"라고 하면 해당 파일에서는 main과 name이 같기 때문에 코드를 실행
# 그렇지 않은 경우 실행 X
# 따라서 다른 파일에서 해당 파일의 함수를 def 된 상태로 import 하여 사용할때
# 자동으로 실행시키지않고 그냥 사용할 수 있도록 함
