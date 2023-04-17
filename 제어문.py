############### if ##################
# 기본 조건
#if 조건:
#    액션
#elif 조건:
#    액션
#else:
#    액선
b = 1
if(b == 1):
    print(b)
elif(b == 2):
    print(b)
else:
    print(b)

# 삼항 연산자 이용
#x = [조건 참 액션] if 조건 else [결과]
o = 'good' if b == 1 else 'bad'


############### while ##################
# 기본 조건
#while 조건:
#    액션
while b < 3:
    b += 1
    print("while문 값 {}".format(b))


############### for ##################
### 기본 조건
#for 조건:
#    액션...
#else:
#    액션...
for i in range(1, 5):
    print("for문 반복 값 {}".format(i))
else: #for문이 끝낫을 때 한번 사용된다.
    print("for문 끝남")



############### 예외 처리 ##################
q = 'abc'
w = 1.23
try: #예상되는 오류 부분 작성
    float(w)
    print("w 정상 끝남")
    float(q)
    print("q 정상 끝남")
except: # 예외 발생시 처리
    print("소수 오류!")
else: # 모든게 정상 처리 됬을때 실행된다.
    print('정상 처리 됨!')
finally: #정상 및 예외 처리 둘다 상관없이 수행함
    print("파이널리??")
