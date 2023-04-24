# function 함수
# 입력 -> 처리 -> 출력
# input을 받아서 특정 작업을 수행하고 output을 반환한다.

# 내장 함수 (built-int)
# print(), len(), zip(), int(), float(), str(), list()

# abs(값)
# 절대값을 반환한다.

# sum(리스트)
# 리스트 안의 숫자를 더한 값을 반환한다.
sum([1,2,3,4])

# max(리스트)
# 리스트 안에서 최대값을 찾아 반환한다.
max([1,2,3,4,5])

# min(리스트)
# 리스트에서 최소값을 찾아 반환한다.
min([1,2,3,4,5])

# chr(정수)
# 정수를 입력받고  해당하는 유니코드 문자를 반환한다.

# ord(문자)
# 문자 1개를 입력합독 해당하는 정수를 반환한다.

# round(값), round(값, 자리수)
# 반올림 함수

# 함수 정의 (define)
# 이름, 입력 값(parameter), 결과 값 (return value)
# def : 함수를 정의하는 명령어
# 함수 이름도 변수 이름 처럼 규칙을 지켜서 지어야한다.

"""
    def 함수이름(함수 입력 값):
        함수기능코드
        return 함수 결과 값
"""

# default params
# input에 기본값을 사용할수 있다.
# list를 기본값으로 사용하면 값이 남아 있다보니 사용하지 않는게 좋다.
# 기본 값이 설정된 매개변수는 기본값이 없는 매개변수보다 뒤에 있어야한다.
def defult_many(a, b=5):
    print(a, b)

# * 를 사용한 매개변수
# 입력값이 몇개가 될지 모를때 사용함
def add_many(*args):
    # 리스트 처럼 사용
    print(args) # 튜플로 출력된다.
add_many(1,2,3,4,5)



# 키워드 매개변수
# **kwargs
# 딕셔너리로 사용한다.
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1, b=2, c=5)


# 함수의 반환
# return 반환 값
# 즉시 종료
# 함수의 반홥 갑슨 무조건 1개이다.
def return_function():
    #return (1, 2) 같은 의미
    return 1, 2



# 별찍기
def print_stars(n):
    for i in range(1, n+1):
        print("*" * i)
print_stars(5)

def print_starts_2(n):
    for i in range(1, n+1)[::-1]:
        print("*" * i)
print_starts_2(5)

def print_starts_3(n):
    for i in range(1, n+1):
        print(" " * (n-i), "*" * (i * 2 -1))
print_starts_3(5)

def print_starts_4(n):
    for i in range(1, n+1)[::-1]:
        print(" " * (n-i), "*" * (i * 2 -1))
print_starts_4(5)

