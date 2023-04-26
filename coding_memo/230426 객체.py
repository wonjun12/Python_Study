# 객체지향 (oop, object oriented programing)
# 객체와 객체 사이의 상호작용으로 프로그램으로 구성하는 프로그래밍 패러다임

# 객체지향의 특징
# 추상화 : 공통된 속성이나 기능 도출 (주요한 특징만 남기는 것)
#   - 변수, 메소드
# 캡슐화 : 데이터의 구조와 연산을 결합한다.
#   - 캡슐하나에 한꺼번에 합친다.
# 상속 : 상위 개념의 특징이 하위 개념에 전달된다.
# 다형성 : 유사 객체의 사용성을 그대로 유지


# 객체는 추상화와 캡슐화의 결과
# 객체는 데이터 필드와 메소드를 가진다.

# 클래스는 객체를 정의한 것(객체의 설계도)
# 데이터 필드(멤버 변수, 속성)
    # - 객체가 가지고 있는 변수
# 메소드
    # - 객체가 가지고 있는 함수


"""
class 클래스이름:
    클래스 맴버 변수
    메소드
"""
# 클래스 이름도 변수 이름 규칙 지켜야한다.
# 클래스 이름 컨벤션 (관용)
    # - 첫 글자 대문자
    # - '_' 안쓰기
    # - 단어 구불될때 대문자

# 클래스 기본 사용 법
class Car:
    def move(self):
        print("move")

class SportsCar:
    pass

# 인스턴스
# 클래스를 통해 생성된 객체
my_car = Car() # 객체를  하나 만들어 변수에 넣음
my_car.move() # 변수를 이용해 메서들 사용
# . => 객체 멤버 접근 연산자
# 파이썬에서는 모든게 객체다.

# type()
# 데이터의 자료형을 반환한다.

# str(문자열) 메소드
# 문자열은 기본적으로 수정 할수 없다. 해당 메서드를 사용해서 재할당해서 값을 변경해야한다.
# upper()
# 모두 대문자로 변경
s = "Hello"
print(s.upper())
# lower()
# 모두 소문자로 변경
print(s.lower())
# strip()
# 문자열 양쪽 끝의 특정 문자를 제거 (공백을 제거할때 사용 많이 한다함.)
s1 = '   Hello   '
print(s1.strip())
# lstrip(), rstrip()
# 좌측, 우측 제거
print(s1.rstrip())
# split()
# 구분자로 분할하여 리스트로 반환
s2 = "hello,world,python"
print(s2.split(","))
# replace()
# 문자열에 특정 부분을 대체, 변경한다.
print(s2.replace(',',' '))


# 객체 만들어 보기
# self 매개변수
# 모든 메소드의 첫번째 매개변수
# 메소드의 정의에는 사용되지만, 호출에는 사용되지 않음
# 객체 자신을 참조하여 클래스에 정의된 멤버의 접근할 때 사용
# 클래스 안에 있는 메서드는 무조건 self가 들어가야한다.

# 멤버 변수를 만들 수 있다.
# 단, 같인 클래스 내에서만 사용할 수 있고 값 할당 전에 다른 곳에서 사용시 오류가 발생한다.

# 맴버 메서드 호출도 가능하다.
# class Person:
#     def say(self):
#         self.name = "셀프 이름 작성"
#         print("Hello")
#     def eat(self, food):
#         print(f"{food} 먹는다.")
#         print(f"{self.name} 출력")
#         self.sleep()
#     def sleep(self):
#         print("잔다")

# person_1 = Person()
# person_1.say()
# person_1.eat("밥")


# initializer
# 초기화할때 동작 방법 및 여부
# __init__ 함수로 무조건 사용 해야한다. (생성과 동시에 초기화를 진행함)
# class Person:
#     def __init__(self):
#         print("initialize")
# print("before")
# person_2 = Person()
# print("after")

# class Person:
#     def __init__(self, name, age, gender, phone):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.phone = phone
#         print("initialize")
#     def say_name(self):
#         print(self.name)
#     def introduce(self):
#         print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}")
# person_3 = Person("이름", 20, "남자", "010-5555-5555")
# person_3.say_name()
# person_3.introduce()


# 상속 inheritance
# 부모 클래스의 정의되어있는 메서드를 전부 사용 할 수 있다.
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"애니멀 {self.name}이 생성됨.")
    def say(self):
        print("")
    def change_aniimal(self, name):
        self.name =name
    # 상속 사용법
    
class Dog(Animal):
    # 부모 클래스와 같은 메서드를 정의했다. = 메서드 재정의, 메서드 오버라이딩
    # 재정의 하면 자식에서 정의된 메서드를 사용한다.
    def say(self):
        print("ㅁ어멍")

my_dog = Dog("검둥이")
my_dog.say()

class Cat(Animal):
    def say(self):
        print("야야옹")
my_cat = Cat("고얭이")
my_cat.say()

class Student:
    def __init__(self, name, age, school, grade):
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade
        print("학생 생성됨")
    def introduce(self):
        print(f"학생의 이름 : {self.name}, 나이 : {self.age}, 학교 : {self.school}, 학년 : {self.grade}")

stu1 = Student("홍", 12, "서울 대", 1)
stu2 = Student("김", 21, "부산 대", 2)
stu3 = Student("대", 35, "중간 대", 3)
stu_list = [stu1, stu2, stu3]
for stu in stu_list:
    stu.introduce()



# 모듈
# 어떤 변수, 함수, 클래스 등 모아놓은 파이썬 파일
# 다른 파이썬 프로그램에서 불러와 사용
# 파이썬에서 모듈은 객체와 같다.
# 모듈을 불러오는 순간 한번씩 전체로 실행된다.
# import 모듈이름

# import t230426_module
# t230426_module.add(1, 2)

# from 모듈이름 import 모듈함수1, 모듈함수2
# from 모듈이름 import *
# from t230426_module import add
# add(1, 2)

# from t230426_module import *
# add(1, 2)


# __name__
# 파이썬을 실행 하는데 실행되는 이름이 정해진다.
# 현재 실행중인 파일에는 __main__의 이름으로 정해지며, import하는 경우 해당 파일의 이름으로 정해진다.


from t230426_module import Calculator
class ZeroCalculator(Calculator):
    def div(self, a, b):
        if b == 0:
            print("0으로 나눌수 없음")
        else:
            print(f"{a} / {b} = {a/b}")

zero_calculator = ZeroCalculator()
zero_calculator.div(10, 0)
print(zero_calculator.mul(10, 2))


# try ~ except
# try 블록에는 오류가 발생할 수 있는 코드
# except 블록에는 오류가 발생 했을 때 수행 할 코드
# 오류가 발생하지 않으면 except 블록의 코드는 실행 되지 않는다.
try:
    100/0
except Exception as e:
    print("에러발생")
    print(e)

# Exception 전체 에러 클래스
# ZeroDivisionError 0으로 나눌려고 하는 에러만 처리
# IndexError 인덱싱 할 수 없음
# finally 예외 발생 여부와 상관없이 항상 수행되는 코드
# else 오류가 발생하지 않으면 실행되는 코드
try: 
    age = int(input("나이: "))
except: 
    print("에러")
else: # 오류가 없을때 실행
    if age >= 20:
        print("성인")

# 미완성일때 완성해라고 안내해줘야 할때
class Brid:
    def fly(self):
        raise NotImplementedError