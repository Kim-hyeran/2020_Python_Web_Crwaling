#Daum에서 뉴스 목록 한 페이지의 기사 제목과 내용 수집(한 페이지 당 15건의 기사)

import requests
from bs4 import BeautifulSoup

#전체 기사 페이지에서 기사마다 접속해 제목과 내용을 크롤링하는 코드

url='https://news.daum.net/breakingnews/digital'

#페이지의 전체 데이터 가져오기
resp=requests.get(url)
soup=BeautifulSoup(resp.text, 'html.parser')

#각각의 기사마다 접속할 수 있도록 하이퍼링크 가져오기
#기사 페이지로 이동하는 하이퍼링크만 가져오도록 목록 부분만 지정
url_list=soup.select('ul.list_allnews a.link_txt')

#각각의 기사에서 제목과 내용 추출
for i in url_list:
    url=i['href'] #기타 태그를 제거하고 기사 주소만 남도록 하는 코드

    resp=requests.get(url)
    soup=BeautifulSoup(resp.text, 'html.parser')
    title = soup.select('h3.tit_view') #<h3 class="tit_view">제목</h3>
    contents = soup.select('div#harmonyContainer p') #<div id="harmonyContainer">내용</div>

    text=''
    for i in contents:
       text+=i.text

    print(title[0].text)
    print()
    print(text)

