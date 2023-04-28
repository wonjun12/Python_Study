def solution(k, score):
    answer = []

    max_score = []
    for i in range(len(score)):
        if i < k:
            max_score.append(score[i])
        elif min(max_score) < score[i]:
            n = max_score.index(min(max_score))
            max_score[n] = score[i]
        answer.append(min(max_score))

    return answer

def solution(k, m, score):
    answer = 0
 
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        answer += min(score[i:i+m]) * m if not len(score[i:i+m]) < m else 0

    return answer


# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지 개수 : N
# 현재 멈춰있는 스테이지 번호가 담긴 stages
# 실패율이 높은 스테이지 부터 내림차순
def solution(N, stages):
    answer = []

    person = {}
    max_person = len(stages)
    for i in range(1, N+1):
        person[i] = stages.count(i) / max_person if stages.count(i) != 0 else 0
        max_person -= stages.count(i)
    person_sort = sorted(person.items(), key= lambda item: item[1], reverse=True)
    
    
    return [i[0] for i in person_sort]

# 다른 사람 코드 속도 차이가 있다.
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
        
    return answer

# 내가 한 풀이
def solution(n, m, section):
    answer = 0

    n_list = [1] * n
    for i in section:
        n_list[i-1] = 0
    
    while n_list.count(0) > 0:
        n_index = n_list.index(0)
        answer += 1
        for j in range(len(n_list[n_index:n_index+m])):
            n_list[n_index+j] = 1

    return answer

# 다른 사람 풀이 한것
def solution(n, m, section):
    paint, answer = section[0]-1, 0
    for v in section:
        if paint < v:
            paint = v+m-1
            answer += 1

    return answer


# 숫자 구하기
def solution(number, limit, power):
    answer = 0

    for i in range(1, number+1):
        result = 1
        n = 2
        while n <= i:
            if i % n == 0:
                result += 1
            n +=1 

        answer += result if result <= limit else power

    return answer
# 찾아낸 방법
def solution(number, limit, power):
    answer = 0

    for i in range(1, number+1):
        result = 0
        for j in range(1, int(i**0.5)+1):
            if i == j**2:
                result += 1
            elif i % j == 0:
                result += 2

        answer += result if not result > limit else power

    return answer

def solution(X, Y):
    answer = ''

    max_length = min(len(X), len(Y))
    

    return answer





a = solution(5, 3, 2)
print(a)
