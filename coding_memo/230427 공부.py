# 표준 라이브러리
# 파이썬에서 지원하는 표준 라이브러리
# 파이썬을 설치할 때 자동으로 함께 설치
# 따로 설치하지 않고 import 명령어로 불러옴

# datetime
# 날짜 관련 라이브러리
# datetime의 date 객체 사용
import datetime
# 날짜 계산 D-일
day1 = datetime.date(2023, 4, 17)
day_end = datetime.date(2023, 9 ,18)
diff = day_end - day1 #날짜 끼리 빼서 남은 일수가 남은다.
print(diff.days)

# 요일 계산
day = datetime.date(2018, 8 , 6)
print(day.weekday())
weekdays = ['월','화','수', '목', '금', '토', '일']
print(weekdays[day.weekday()])
#   0   1   2   3   4   5   6 
#   월  화  수  목  금  토  일

# datetime의 포맷팅 코드
# 날짜랑 시간 표시하는 방법
# 서로 다른 표기법에 대한 해결 파이썬의 방법
today = datetime.datetime.today()
print(today)
# strftime()
# 원하는 방식으로 표기 가능
print(today.strftime("%Y년 %m월 %d일"))
# %Y 년도 4자리
# %y 년도 2자리
# %m 월
# %d 일
# %H 24시간
# %I 12시간
# %M 분
# %S 초
# %A 요일

# time 라이브러리
# 시간 관련 라이브러리
import time
# time()
# 1970년이후부터 지금까지 초 (UTC로 기준으로 나옴)
time_now = time.time()
print(time_now)
print(time.strftime("%H:%M:%S", time.localtime(time_now)))

# sleep()
# 잠시 프로그램을 멈춤 (초 단위)
time.sleep(1)

# math
# 수학관련 라이브러리
import math
# 올림
math.ceil(1.1)
# 내림
math.floor(1.9)
# 파이 출력
print(math.pi)


# random
# 난수 관련
import random
# random() 랜덤 소수 반환
# 0.0 ~ 1.0 사이 실수 난수 값
rand_number = random.random()
print(rand_number)

# randint(시작, 끝)
# 특정 정수의 사이의 랜덤한 정수 값
rand_number = random.randint(1, 10)
print(rand_number)

# choice(리스트)
# 리스트 요소 중 무작위로 하나를 반환
rand_lists = ["밥", "국", "반찬"]
rand_list = random.choice(rand_lists)
print(rand_list)

# shuffle(리스트)
# 리스트의 순서를 무작위로 변경한다.
random.shuffle(rand_lists)
print(rand_lists)

# 로또 만들기
lotto_num = list(range(1, 46))
random.shuffle(lotto_num)
print(lotto_num[:6])

# in 연산자
# '검색할 값' in 전체 값 ('리스트, 튜플, 문자열')
# a in b
# a가 b에 포함되어 있는지 확인한다.



# os
# OS 자원을 제어
import os
# os.environ
# 시스템의 환경 변수 값을 리턴한다.
#print(os.environ)

# os.getcwd()
# get current working directory
# 현재 작업 위치
print(os.getcwd())

# os.mkdir(디렉터리)
# 폴더를 만든다.
# os.mkdir("테스트 폴더")

# os.rename(원래이름, 바꿀이름)
# 파일의 이름을 바꾼다.

# os.rmdir(디렉터리)
# 폴더를 지운다.
# 폴더가 비어있어야 삭제 가능

# os.unlink(파일)
# 파일을 지운다.

# os.path
# os.path.exists("경로")
# 해당 경로의 파일이 존재하지는 판별하는 함수

# os.path.join("경로", "경로", "경로")
# 경로를 합쳐서 1 개의 경로로 만들어준다.
# cwd = os.getcwd()
# my_folder = "file_test"
# file_name = "test_file.txt"
# file_path = os.path.join(cwd, my_folder, file_name)
# with open(file_path, "w", encoding="UTF-8") as f:
#     f.write("테스트")


# 외부 라이브러리
# 파이썬 표준 라이브러리가 아닌 라이브러리 pip를 사용해서 설치한다.

# pip
# package installer for python
# 파이썬 모듈, 패키지 설치하는 도구
# import numpy, pandas, matplotlib, scikit-learn, keras, Tensorflow, opencv, django, flask
# PyPI (Python Package index) 파이썬 소프트웨어 저장 공간
# 파이썬 패키지를 설치해준다.

# pip list
# 설치된 패키지 확인

# pip install 패키지이름
# 패키지 최신 버전 설치

# pip install 패키지이름==1.0.5
# ==, <=, >= 으로 특정 할 수 있음
# 패키지 특정 버전으로 설치

# pip install --upgrade 패키지이름
# 해당 패키지 최신 버전으로 업데이트

# pip uninstall 패키지이름
# 패키지 삭제