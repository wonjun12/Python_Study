# 거꾸로 배열해도 같은 단어 또는 문장이 되는 
# 회문(palindrome)인지 판별하는 함수를 정의하세요.
# 함수에 문자열을 입력 받고 회문이면 True 아니면 False를 반환하도록 정의하세요.
# 함수이름 : is_palindrome
# 반환 값: True 또는 False

# def is_palindrome(input_string):
#   drome("다시 합창합시다")
# print(a)  input_string = input_string.replace(' ','')
#     return input_string == input_string[::-1]

# a = is_palin


# 데이터 끌고도온다.
# crwaling
# 데이터 수집 -> 데이터 분석/처리 -> 인공지능 모델 학습 ->

# http (hypertext transfer protocol)
# request - response
#  요청   -   응답
# client  -  server

# html 파싱 (hypertext markup language)
# 웹사이트를 표현하기 위한 언어
# ModuleNotFoundError: No module named 'requests'
# 외부 라이브러리 이므로 설치해야한다.
import requests

url = "https://www.naver.com/"
response = requests.get(url)
status = response.status_code
html = response.text
print(status)

# http 상태 코드
# 200 : ok
# 요청 성공
# 302 : 리다이렉트
# 다른페이지로 바로 연결
# 400 : Bad Request 요청이 잘못됨
# 401 : Unauthorized 비인증
# 403 : Forbidden 접근 권한 없음
# 404 : Not Found 경로를 찾을수 없다./ 요청 받은 내용이 없음 
# 405 : Method Not Allowed 접근 방법 잘못됨
# 500 : Internal Server Error 서버 에러
# 501 : Not Implemented 
# 502 : Bad Gateway 잘못된 응답

# url 구조
# 프로토콜://호스트주소:포트번호/경로?쿼리
# http://naver.com/?~~~
# ? 뒤에 오는 값들을 Query라고 부른다.

# get을 통해 가져오면 String으로 가져오게되는데 보기 쉽게 만들어 주는게 있다.

# BeautifulSoup4
# html 파싱 (parsing)
# html을 객체 구조화 해서 사용한다.
# 외부 라이브러리이므로 설치 해야한다.
from bs4 import BeautifulSoup
# html 태그
# <태그이름 속성=속성값> 내용 </태그이름> 
# html.head
# html.body 처럼 사용할 수 있게 해줌
html  = "<html><body>Hello</body></html>"
soup = BeautifulSoup(html, "html.parser")
print(soup.body)
print(soup.body.text)



# import requests
# from bs4 import BeautifulSoup
# search_url = "https://www.google.com/search?tbm=isch&q="
# keyword = "맥주"
# url = search_url + keyword
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# # print(soup.body)
# print(soup.find('div')) # 맨 앞을 찾아서 반환한다.
# print(soup.find_all('div')) # find_all 전부 찾아서 list로 반환한다.
# imgs = soup.find_all('img')
# import os
# folder_name = 'imgs'
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)

# for dix, img in enumerate(imgs[1:]):
#     file_name = f"img_{dix}.jpg"
#     file_path = os.path.join(folder_name, file_name)
#     img_response = requests.get(img['src'])
#     img_data = img_response.content
#     with open(file_path, "wb") as f:
#         f.write(img_data)


# enumerate(이터러블)
# 반복되는 변수를 key,value로 변환하여 반환한다.
# li = ['a','b','c']
# for idx, name in enumerate(li):
#     print(idx, name)

import requests
from bs4 import BeautifulSoup

import os
folder_name = "test_string_Crawling"
file_name = 'headlines.txt'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
file_path = os.path.join(folder_name, file_name)

headers = {"User-Agent":"Mozilla/5.0"}
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'
response = requests.get(url, headers = headers)
html = response.text
soup = BeautifulSoup(html, "html.parser")
div = soup.body.find('div', attrs={'class': 'list_body'})
headlines = div.find_all('a', attrs={'class' : 'cluster_text_headline'})


for headline in headlines:
    response = requests.get(headline['href'], headers = headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    div_texts = soup.body.find('div', attrs={'id' : 'dic_area'}).find_all(text=True)
    # a는 경로에 자동으로 폴더를 만들 수 없다.
    # w는 경로에 자동으로 폴더를 만든다.
    with open(file_path, 'a', encoding="UTF-8") as f:
        f.write(f"{headline.text.strip()}\n")
        for div_text in div_texts:
            f.write(f"{div_text}")
        
        f.write(f"==========================================\n")



