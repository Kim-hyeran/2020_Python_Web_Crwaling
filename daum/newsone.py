#Daum에서 뉴스 한 건의 기사 제목과 내용 수집

import requests
from bs4 import BeautifulSoup

url="https://news.v.daum.net/v/20200616060010828"

#requests : 단순히 데이터를 가져오는 역할만 수행
resp=requests.get(url)

#경로가 옳게 설정 되었는지 아닌지 판단
#resp에 status_code가 200이면 성공, 아니면(나머지는) 실패
if resp.status_code==200 :
    print('Success')
else :
    print('Wrong URL')

#BeautifulSoup(원하는 데이터만 추출하기 위한 도구)에 input으로 resp의 값(웹사이트의 소스코드 전체) 전달
soup=BeautifulSoup(resp.text, 'html.parser') #soup에 엡사이트의 소스코드 전체가 저장됨
#태그가 복수 개로 존재할 수 있기 때문에 결과값을 [list]로 받아온다
title=soup.select('h3.tit_view') #.select()를 이용하여 원하는 정보만 추출
contents=soup.select('div#harmonyContainer p') #자손선택자 p
#soup.select()는 return을 무조건 list type으로 반환 : [val1, val2, val3, ...]

#text만 추출
print(title[0].text) #list type으로 반한되었기 때문에 list type으로 출력 코드 작성
print()

#데이터 중간의 공백까지 전부 제거하여 출력하기
text=''
for i in contents :
    text+=i.text

print(text) #strip : 데이터의 앞뒤에 존재하는 공백만 제거