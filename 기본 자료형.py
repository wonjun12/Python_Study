# 다른 언어와 달리 타입 선언을 할 필요가 없다.
a = 2

# 특정 함수안에 사용시 괄호가 존재하는 것이 아닌 띄어쓰기하면 된다. (Tab)
if a == 1:
    print(a)

# 문자열을 작성 가능하다.
str = "파이썬을 배운다."
# 문자열의 특정 범위를 가져올수있다.
print(str[:3])
print(str[5:7])

############### 리스트 ##################
# 리스트 => 배열과 비슷하다.
T_list = [1, 2]
# 리스트의 요소 개수
# len(변수)
print(len(T_list))
# 리스트의 요소를 특정 위치 추가
# 변수.insert(위치, 값)
T_list.insert(0, 5)
print(T_list)
#리스트의 요소를 맨뒤에 추가
T_list.append(7)
print(T_list)
#리스트 역순 정렬
T_list_Reverse = sorted(T_list, reverse=True)
print(T_list_Reverse)
T_list.sort(reverse=True)
print(T_list)
#리스트의 위치 반환 => 찾는 값의 위치를 반환함
print(T_list.index(5))
#리스트의 요소를 추출하고 삭제한다. 
#   -> 해당 번호의 위치에 있는 값 추출하면서 리스트에서 삭제한다.
print(T_list.pop(1))
print(T_list)
# 인덱싱과 슬라이싱 
#   -> 리스트는 곧 문자열과 비슷하기에 추출법이 비슷하다.
str_list = ['파이썬', '프로그램', '빅데이터', '위한']
print(str_list[0])
    #리스트 마지막 첫번째 값
print(str_list[-1])
    # ~ : ~
    # 시작 : 끝
print(str_list[-2:]) #마지막 2번째에서 마지막 까지
print(str_list[:2]) #처음부터 2번째 까지



############### 튜플 ##################
# 리스트와는 다르게 수정, 삭제가 불가능하다. => const와 비슷
# 튜플의 생성
T_tuple = (5, 2, 3)
print(T_tuple)
# 튜플의 길이
print(len(T_tuple))
# 다른 변수에 튜플을 넣을수 있다.
new_T_tuple = '21', '123', T_tuple
print(new_T_tuple)



############### 딕셔너리 ##################
# Key와 Value의 쌍으로 갖는 자료형
# 쉽게말하면 객체의 형태를 말한다.
# key에는 리스트가 불가능하다. -> 유일하기 때문에
Human = {
    #key   :  value
    '정보' : '과학',
    '배움' : '이론'
}
print(Human)
# keys(), items()
print(Human['정보']) # key로 value 반환
print(Human.items()) #key와 value들을 리스트의 튜플로 변환하여 반환한다.
print(Human.keys()) #key들을 리스트의 형태로 변환하여 반환한다.
# for 활용법
for key, values in Human.items():
    print('{}는 {}'.format(key, values)) #.format을 통해 {}에 값을 넣을수 있다.



############### 집합 ##################
# 정렬되지 않은 단순 객체의 묶음
# 중복되며, key가 없는 객체의 형태와 비슷하다.
bri = set(['brazil', 'russia', 'india'])
print(bri)
print('brazil' in bri)
print('brazil in' in bri)
# 집합의 다르 객체로 복사 가능하다.
bric = bri.copy()
print(bric)
bric.add('korea') # 원소 추가
print(bric)
# 원소 집합간 포함 관계
print(bric.issuperset(bri)) # bric안에 bri가 포함이 되는지
print(bri.issuperset(bric)) # bri안에 bric이 포함이 되는지
# 원소 삭제
bri.remove('brazil')
# 교집합 출력
print(bri & bric)
