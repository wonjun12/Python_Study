def solution(ability):
    answer = 0
    
    childe = {}
    
    length = len(ability[0])
    for n in range(length):
        max_score = 0
        for key, value in enumerate(ability):
            childe[key] = value
        for v in range(length):
            childe_list= []
            for score in childe.values():
                childe_list.append(score[v-n])
            max_score += max(childe_list)
            childe[childe_list.index(max(childe_list))] = [ -1 for i in childe[childe_list.index(max(childe_list))]]
        answer = max(answer, max_score)

    return answer

# from itertools import permutations
import itertools as it
def test(abi):
    answer = 0
    p = list(it.permutations(abi, len(abi[0])))
    
    for i in range(len(p)):
        total = 0
        for j in range(len(p[i])):
            total += p[i][j][j]
        answer = max(answer, total)
    print(answer)
    return answer

a = solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]])
a = test([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]])


import itertools as it_tools
def solution(ability):
    answer = 0
    
    ab_list = it_tools.permutations(ability, len(ability[0]))
    
    for child_list in list(ab_list):
        total = 0
        for i in range(len(child_list)):
            total += child_list[i][i]
        answer = max(answer, total)

    return answer



c1 = [1, 2]
ca = ('A', 'B')
c = it_tools.chain(c1, ca)
print(list(c))