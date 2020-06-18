#Daum에서 뉴스 목록 여러 페이지의 기사 제목과 내용 수집(한 페이지 당 15건의 기사)

import requests
from bs4 import BeautifulSoup

cnt=0

#목록 페이지 주소 지정 및 범위 설정
for i in range(1,4):
    url='https://news.daum.net/breakingnews/digital?page={}'.format(i)

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    #기사 목록에서 제목에 걸린 링크만 수집
    url_list = soup.select('ul.list_allnews a.link_txt')

    for j in url_list: #기사 목록 한 페이지의 데이터 전부 수집
        cnt+=1 #수집한 데이터의 갯수 세기
        url = j['href'] #기사 한 개의 url 꺼내오기

        resp = requests.get(url) #url 주소를 이용해서 해당 웹페이지의 모든 소스코드를 불러와 resp에 저장
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.select('h3.tit_view')
        contents = soup.select('div#harmonyContainer p')

        text = ''
        for k in contents:
            text += k.text

        print(title[0].text)
        print()
        print(text)
        print()

print('▶▶{}건의 뉴스 기사를 수집하였습니다.'.format(cnt))