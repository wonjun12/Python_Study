# while 반복문
"""
while 조건:
    반복할 코드
"""
# 조건이 참인 경우 코드를 계속 반복
n = 1
while n < 10:
    print(n)
    n += 1


# += 연산자
# 대입 연산자의 일종
# 더하기 연산 후 할당
# n += 1 은 n = n +1 이라는 의미
# -=, *=, /=, **=, //=, %=


# break
# 반복문을 즉시 종료한다.
while n < 10:
    print('break 사용')
    break

####
# while 반복문을 활용하여 1부터 10까지 홀수만 출력한다.

# continue
# 반복문의 제일 처음으로 돌아감

# 무한 반복문
# 무한 루프
# 조건식에 True를 입력해 항상 참
#while True:
    #print("hi")


# 무한 반복문으로 계산기 만들기
# +, -, *, / 계산
# 2개의 수를 계산
# while True:
#     print("""
#     계산기
#     ==========
#     1. 더하기
#     2. 빼기
#     3. 곱하기
#     4. 나누기
#     """)
#     operator = input("계산방식을 선택하세요 : ")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if operator == '1':
#         print("계산 : {} + {} = {}".format(num1, num2, num1+num2))
#     elif operator == '2':
#         print("계산 : {} - {} = {}".format(num1, num2, num1-num2))
#     elif operator == '3':
#         print("계산 : {} * {} = {}".format(num1, num2, num1*num2))
#     elif operator == '4':
#         print("계산 : {} / {} = {}".format(num1, num2, num1/num2))
#     else:
#         print("잘못 된 입력 방식입니다.")
#         break

# 계산기 만들기



# while 반복문을 사용해서
# scores 리스트에 시험 점수 5개를 정수
# 형으로 입력받으세요
# scores = []
# max_scores = 5
# while len(scores) < max_scores:
#     scores.append(int(input("{}번째 시험 점수를 입력하새요 : ".format(len(scores)+1))))
# print("시험 점수를 출력합니다 : ", scores)



# for 문
"""
for 변수 in iterable값:
    반복할 코드
"""
li_1 = ["one", "two", "tree"]
for i in li_1:
    print(i)
# 첫번째 요소부터 마지막 요소까지 변수에 대입하면서 반복
s1 = "hello"
for i in s1:
    print(i)

# range()
# 숫자 range 객체를 만들어 주는 함수
# range(끝 정수), range(시작, 끝), range(시작, 끝, 스텝)

# pass, continue
# pass는 다음 으로 넘어가는 것이고, continue는 다음 반복문으로 넘어간다는 것이다.

# reversed를 사용해서 뒤집기 가능
for i in reversed(range(1, 11)):
    print(i)

for i in range(1, 11)[::-1]:
    print(i)
# 슬라이싱  [시작인덱스:끝인덱스 : 방향]


# 2중 for 문
for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i*j))


# git의 vascode 확인법
# Source Control에 보면 변경되는 것을 한눈에 확인할 수 있다.
# Commit > 자신의 컴퓨터 로컬 리포지토리에 한번 저장한다.
# Push > Commit한 자신의 저장된 리포지토리를 Git서버에 저장한다.

# git에 넣는데 이름과 이메일 오류 발생시
# git config --global user.name "wonjun12"
# git config --global user.email "wjdaks333@naver.com"


# git add .
# git commit -m "Add python files"
# git push