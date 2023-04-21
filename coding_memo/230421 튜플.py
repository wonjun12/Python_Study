# 튜플 tuple형
# 데이타 타입 중 하나
# 값이 정해지면 값을 수정할 수 없다.

# mutable(수정가능) / immutable(수정 불가능)
# mutable 종류
# list, dict

# immutable 종류
# int, float, str, tuple

# 다른 언어에서는 값을 할당해서 적용시키지만 Python은 값에 대한 주소로 가르킨다.
# 즉, 처음부터 값은 기본적으로 값이 할당 되어있고 사용자가 값을 넣는것은 가르키는 것을 말한다.
# 그래서 값을 할당한 변수에 대해 다른 변수에 복사 할려할때, 완벽히 복사되는것이 아닌 같은 곳을 바라보는 변수로 변경된다.
# 그래서 Tuple은 해당 주소로 확정 짓는 것이고, List는 주소를 변경 할수 있다는 차이가 있다.


# 튜플 사용
tuple1 = ("Hello", "world")
tuple2 = (1,2,3,4)
tuple3 = (1, 2, "hEllo")
tuple4 = 1, 2, 4
tuple5 = (1,2, (3,4,5))
tuple6 = (1,2, [1,2,3,4], {1:2, 3:4})
tuple6[2][1] = 3
# 튜플은 수정 할수 없지만 튜플 안에 리스트같은경우 수정가능하다.

# +, *를 할수 있다.
# 해당 값으 수정을 하는것이 아니라 합쳐서 새롭게 만든다음 반환하기에 가능하다.
t1 = tuple1 * 3
t2 = tuple2 + tuple6

# 슬라이싱, 인덱싱 가능하다.
print(tuple3[2])
print(tuple3[0:1], tuple3[0:2], tuple3[0:0]) # 튜플로 꺼냇기 때문에 수정 불가능하다.
print(len(tuple3))

# 튜플은 정렬하지 못한다. 정렬하면 값이 변경되기때문이다.
# 단일 튜플의 값을 정하거나 가져올때 ','를 하나 붙여서 튜플로 정해진다.
# 만약 없이 한다면 (1) int로 정해진다.
print(type((1)), type((1,)), type([1]), type({1}))

# for 문 사용 가능

for i in tuple3:
    print(i)

# while not 2 <= n <= 9 가능하다.
result = int(input("숫자를 입력 : "))
print(int((result-1)**0.5)**2)


# zip()
# 길이가 같은 list를 묶어서 for문 등으로 사용 가능한 iterable을 반환한다.
z1 = [1,2,3]
z2 = [3,4,5]
for x, y in zip(z1, z2):
    print(x+y)



# 3, 6, 9 게임을 모티브로 작성한 코드
# 3, 6, 9 마다 짝을 출력, 나머지는 숫자 출력 (배수가 아닌 숫자를 본다)
n = int(input("정수 : "))
for i in range(1, n+1):
    answer = i
    for s in str(i):
        if int(s) % 3 == 0 and s != '0':
            answer = "짝"
            break
    print(answer)


# 정수를 입겱 받고 그 정수의 약수를 모두 출력하세요.
# 약수 : 나누었을 때 나머지가 0으로 떨어지게 하는 수
