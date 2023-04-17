############### 함수 정의 ##################
# 기본 함수 정의
def Function_Sum(a, b):
    print("함수가 호출됨")
    return a + b

Numbers = Function_Sum(1, 3)
print(Numbers)

#디폴트 함수 정의가 가능하다. 
#인자를 받는 변수에 값을 임의로 넣는다면 기본값이 된다
def Function_default(a, b = 0):
    print("디폴드 정의 함수 호출")
    return a + b

print(Function_default(1, 2))
print(Function_default(1))


############### 전역 / 지역 변수 ##################
# 전역 변수와 지역 변수의 차이는 확실하다.
# 전역변수에 사용하는 이름이 있다고 한다면, 인자가 있어야만 지역변수에 같은 이름을 선언할수 있다.
x = 10
def T_Func(x):
    print(x)
    x = 5
    print(x)
T_Func(x)

# 단, global를 사용한다면 따로 인자를 받지 않아도 가능하긴하다.
y = 10
def T_Func2():
    global y
    print(y)
    y = 1
    print(y)
T_Func2()