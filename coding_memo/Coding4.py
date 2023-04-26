# combinations 사용
# import itertools as ite;
# def solution(number):
#     answer = 0
    
#     for n_list in ite.combinations(number, 3):
#         if sum(n_list) == 0:
#             answer += 1
    
#     return answer

# 알파벳 정렬
# sorted에서 key를 이용해 lambda를 사용한다.
# def solution(strings, n):
#     answer = sorted(strings, key=lambda x: (x[n], x)) 
#     return answer



# rfind, rindex
# def solution(s):
#     answer = []
    
#     for i in range(len(s)):
#         if s[i] in s[0:i]:
#             answer.append(i - s[0:i].rfind(s[i]))
#         else:
#             answer.append(-1)
    
#     return answer

def solution(n):
    answer = [2]
    
    for num in range(2, n+1):
        if num % 2 == 0:
            continue
        div_num = 2
        while div_num <= num:
            if num % div_num == 0:
                if num == div_num:
                    answer += 1
                break
            div_num += 1
    return answer


# 에라토스테네스의 체
def solution(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, n + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

def solution(n):

    sieve_list = [True] * (n+1)

    for i in range(2, n+1):
        if sieve_list[i] == True:
            for j in range(i*2, n+1, i):
                sieve_list[j] = False

    return sieve_list.count(True) -2


print(solution(5))