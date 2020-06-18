import requests
from bs4 import BeautifulSoup

cnt=0
page=1
compare_writer=''
break_point=False # 이중 반복문을 빠져나가기 위한 조건

# 리뷰가 작성된 페이지는 영화마다 수가 다르고, 설정한 페이지에서도 추가/삭제 등의 변경사항이 있을 수 있기 때문에
# 유한한 횟수를 반복하는 for 반복문 대신 while 반복문을 사용한다
while(True):
    url='https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=191436&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)

    resp=requests.get(url)

    if resp.status_code!=200:
        print('존재하지 않는 URL입니다')

    soup=BeautifulSoup(resp.text, 'html.parser')
    grade_list=soup.select('div.score_result li')

    #페이지 가장 첫 번째(가장 상단) 리뷰 작성자의 인덱스 번호를 알기 위해 enumerate 사용
    for i, grade in enumerate(grade_list):
        privious_writer=grade.select('div.score_reple a>span')[0].text.strip() #작성자
        cut_index=privious_writer.find('(') #작성자의 닉네임만 추출하기 위한 index번호 계산
        contents=grade.select('div.score_reple>p>span')[0].text.strip() #리뷰 내용
        score=grade.select('div.star_score>em')[0].text.strip() #평점
        reg_date=grade.select('div.score_reple em')[1].text.strip() #날짜

        #영화 리뷰 작성자명에 닉네임 존재 여부에 따라 출력 방식이 다름(예:닉네임(id****) 혹은 id****)
        #이런 경우 닉네임만, 혹은 아이디가 출력되도록 조건문을 사용
        if cut_index>0: #기본값이 -1이기 때문
            writer=privious_writer[:cut_index]
        else:
            writer=privious_writer

        #현재 작성자 수집

        # 네이버의 경우 마지막 페이지를 초과하는 페이지로 접속해도 리뷰의 마지막 페이지를 실행시키기 때문에
        # 작성자(영화 당 한 개의 리뷰만 작성할 수 있음)의 중복 여부를 따져 반복문을 중단시킬 수 있다

        # 영화 리뷰 수집 페이지의 마지막을 계산하는 코드
        if i==0:
            if compare_writer==writer: # 매 페이지의 첫 번째 게시글의 작성자를 compare_writer에 저장
                print('데이터 수집이 완료되었습니다.')
                break_point=True
                break # 매 페이지의 첫 번째 게시글 작성자와 compare_writer를 비교해 일치하면 중복 페이지 판단
            else:
                compare_writer=writer

        print('★★★★★ 게시글', (cnt+1), '★★★★★')
        print('작성자 :', writer)
        print('리뷰 :', contents)
        print('평점 :', score)
        index_val = reg_date.index(' ')
        print('날짜 :', reg_date[:index_val])
        print()

        cnt += 1

    # while 반복문까지 벗어나도록 하는 코드
    if break_point:
        break

    page+=1

print('영화 리뷰를 {}건 수집하였습니다.'.format(cnt))