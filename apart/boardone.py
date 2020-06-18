import requests
from bs4 import BeautifulSoup

url='http://news.sarangbang.com/talk/bbs/story/163962?url=%2F%2Fnews.sarangbang.com%2Fbbs.html%3Ftab%3Dstory'

resp=requests.get(url)

if resp.status_code!=200:
    print('WARNING : 잘못된 URL 접근입니다')

soup=BeautifulSoup(resp.text, 'html.parser')

title=soup.select('h3.tit_view')[0].text.strip()
contents=soup.select('div.bbs_view p')
reg_dt=soup.select('span.tit_cat')[1].text.strip()[:10] #페이지 구조가 같을 경우에만 사용 가능
writer=soup.select('a.name_more')[0].text.strip()

print('TITLE : ', title)
print('WRITHER : ', writer)
print('DATE : ', reg_dt)

text=''
for i in contents:
    text+=i.text.strip()
print('CONTENTS : ', text)