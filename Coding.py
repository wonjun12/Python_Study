# 정렬 후 중앙 값 들고오기
sorted(array)[len(array) // 2]

#한줄 for str 적용
''.join(i*n for i in my_string)

#문자열 자르기 (특정 문자를 찾아서 변경하는 함수)
my_string.replace(letter, '')


"".join([i for i in my_string if not(i in "aeiou")])

[i for i in range(1, n+1, 2)]


len(set(s1)&set(s2))

#숫자를 문자열로 변환해서 for로 돌린다.
sum(int(i) for i in str(n))

#특정 10자리 이상 숫자를 문자로 변경하는것 (10 -> 1과 0을 들고옴)
return ''.join([chr(int(i)+97) for i in str(age)])

# 문자열안에 문자열을 찾는 방법
1 if str2 in str1 else 2

# **은 제곱인데 0.5를 대입하면 제곱근이 된다. => 1/2니까
i**0.5

# 문자 대소문자 동시에 전체 변경
my_string.swapcase()

#비트 연산자... 개쩐다
n << t

#문자열에서 숫자 판별 함수
c.isdigit()

# max(숫자, 숫자)
max 함수는 해당 숫자 및 배열들을 비교해 큰 값들을 반환합니다.
#min(숫자, 숫자)
max와 동일하다.

# 특정 문자열에서 2개의 문자만 서로 위치를 교환함 -> list를 사용해서 변경한다.
s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)