# 파일 입출력
# 파이썬에서 파일 생성, 수정

# open()
# 파이썬 내장 함수
# 파일을 열고 파일 객체를 리턴한다.
# open(파일 이름, 파일 열기 모드)
# f = open("C:/Users/405/Python_Study/file_test/새파일.txt", 'w') # 해당 파일이 없다면 생성함.
# f.close() # open으로 연 파일은 clese로 무조건 닫아야한다.


# 절대 경로
# C:/, D:/ 최 상단 경로부터 나타낸 경로

# 상대 경로
# 현재 작업 위치 부터 나타낸 경로


# 파일 열기 모드
# r : read, 읽기 모드, 파일을 읽기만 할 때 사용
# w : write, 쓰기 모드, 파일에 내용을 쓸 때 사용
# a : add, 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용

# 인코딩 UTF-8 변환
# 쓰기
# w => 덮어 쓰기
# f = open("./file_test/새파일.txt", "w", encoding="UTF-8")
# for i in range(1, 11):
#     f.write(str(i) + "번째 줄\n")
# f.close()

# 쓰기
# a => 이전의 있던 내용 유지, 다음 내용 추가 사용
# f = open("./file_test/새파일.txt", 'a', encoding="UTF-8")
# for i in range(11, 21):
#     f.write(str(i) + "번째 줄\n") 
# f.close()

# 읽기
# f = open("./file_test/새파일.txt", 'r', encoding="UTF-8")
# readline() 첫번째 한줄만 읽는다. => 한줄 읽고 다음 줄로 이동된다.
# 커서가 이동하는 것처럼 읽어옴
# line = f.readline() #1번째 줄\n
# print(line)
# line = f.readline() #2번째 줄\n
# print(line)
# while True:
#     line = f.readline()
#     if line == "":
#         break
#     print(line)
# f.close()

# readlines()
# 파일의 모든 줄을 읽어서 리스트로 반환
# lines = f.readlines()
# for line in lines:
#     print(line, end="")
# f.close()

# read()
# 파일 내용 전체를 문자열로 반환한다.
# data = f.read()
# print(data)
# f.close()

# 함수를 사용하지 않고 바로 읽기
# 파일 객체를 이용해 바로 읽는 방법
# for line in f:
#     print(line)
# f.close()

# with 문
# open - close를 자동으로 해준다.
# with를 나가면 close가 자동으로 완료되었기에 나가면 작동되지 않는다.
# with open("./file_test/새파일.txt", 'a', encoding="UTF-8") as f:
#     f.write("end of file")

# csv(comma separated values)
# , 로 구분되는 값들을 모아놓은 파일
# 이름, 입실시간, 퇴실시간
# with open("./file_test/data.csv", "w", encoding="UTF-8") as f:
#     f.write("날짜, 날씨, 기온\n")
#     f.write("20230424, 맑음, 10\n")
#     f.write("20230425, 비, 10\n")

# with open('./file_test/data.csv', 'r', encoding="UTF-8") as f:
#     data = f.readlines()
#     print(data)

# 계산 결과 저장 함수
# 정수 2개를 입력 받고 두 수의 더한 결과를 add_result.txt 파일에 저장하는 함수 정의
# def add_write(a, b):
#     with open('./file_test/add_result.txt', 'a', encoding="UTF-8") as f:
#         f.write("{} + {} = {}\n".format(a, b, a+b))
#     print("저장 완료")
# num1 = int(input("더할 첫번째 수를 입력하세요 : "))
# num2 = int(input("더할 두번째 수를 입력하세요 : "))
# add_write(num1, num2)


# 계산기 만들기
# 기능 : 두 정수의 사칙연산 (+,-,*,/)
# add(), sub(), mul(), div() 함수 정의
# input() 함수를 활용하여 정수 2개, 사칙연산 선택을 입력받은 후 계산 결과를 print한다.
# 계산식과 결과를 calculator_result.txt.파일에 기록한다.
# 사용 자가 'q' 를 입력하면 종료한다.

def add(a, b):
    return int(a) + int(b)
def sub(a, b):
    return int(a) - int(b)
def mul(a, b):
    return int(a) * int(b)
def div(a, b):
    return int(a) / int(b)
def file_save_func(string):
    print('결과 : {}'.format(string))
    with open("./file_test/calculator_result.txt", 'a', encoding="UTF-8") as f:
        f.write(string+'\n')

# while True:
#     print("종료 하실려면 'q'를 입력하세요.")
#     num1 = input("첫번째 수를 입력하세요 : ")
#     if num1 == 'q':
#         break
#     cal = input("계산할 기호를 입력하세요(+, -, *, /) : ")
#     if cal == 'q':
#         break
#     num2 = input("두번째 수를 입격하세요 : ")
#     if num2 == 'q':
#         break

#     if cal == '+':
#         result = add(num1, num2)
#     elif cal == '-':
#         result = sub(num1, num2)
#     elif cal == '*':
#         result = mul(num1, num2)
#     elif cal == '/':
#         result = div(num1, num2)
#     else:
#         print('잘못 된 입력입니다.\n')
#         continue
#     result_string = '{} {} {} = {}'.format(num1, cal, num2, result)
#     file_save_func(result_string)


# 문자열 포매팅 (formatting)
num1 = 5
num2 = 2
result = "%d + %d = %d" % (num1, num2, num1+num2)
print(result)
# 포멧 코드
# %s 문자열 (string)
# %d 정수 (int)
# %f 실수 (float)
# %o 8진수
# %x 16진수
## %% % 글 사용

# f-string
# 정말 유용하게 사용됨 Python 3.6이후 사용됨
result_s = f"{num1} + {num2} = {num1 + num2}"
print(result_s)

