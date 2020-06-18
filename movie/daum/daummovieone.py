import requests
from bs4 import BeautifulSoup
import movie.persistence.MongoDAO as DAO # 생성한 class를 업로드할 데이터 파일에 불러오기

# 객체 생성
mDAO=DAO.MongoDAO()

cnt=0
page=1

while(True):
    url='https://movie.daum.net/moviedb/grade?movieId=126335&type=netizen&page={}'.format(page)

    resp=requests.get(url)

    if resp.status_code!=200:
        print('잘못된 접근입니다')

    soup=BeautifulSoup(resp.text, 'html.parser')
    grade_list=soup.select('div.review_info')

    #while 반복문이 무한으로 실행되지 않도록 리뷰 페이지가 끝나면 종료시키는 코드
    #daum의 경우에는 오류가 아닌 빈 페이지를 실행시키기 때문에 아래 if구문으로 중단시킬 수 있다
    if len(grade_list)==0:
        print('마지막 페이지입니다')
        break

    #댓글 형식의 페이지는 수집한 전체 데이터를 낱개로 다시 가져오는 과정 필요

    print(page, 'page *****************************************************************')
    print()

    for grade in grade_list:
        cnt+=1

        writer=grade.select('em.link_profile')[0].text.strip()
        score=grade.select('em.emph_grade')[0].text.strip()
        contents=grade.select('p.desc_review')[0].text.strip()
        reg_date=grade.select('span.info_append')[0].text.strip()

        #데이터가 일부만 가져와질 때(<br>태그가 합쳐진 경우)는 BeautifulSoup으로는 해결할 수 없다(Selenium 사용)

        print('작성자 :', writer)
        print('평점 :', score)
        print('리뷰 :', contents)
        index_val=reg_date.index(',')
        print('날짜 :', reg_date[:index_val])
        print()

        # MongoDB에 저장하기 위해 Dict Type으로 변환
        data={'content':contents, 'writer':writer, 'score':score, 'reg_date':reg_date}

        # 내용, 작성자, 평점, 작성일자를 MongoDB에 Save
        mDAO.mongo_write(data)

    page+=1

print('▶▶영화 리뷰를 {}건 수집하였습니다'.format(cnt))