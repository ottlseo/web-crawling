import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r/")
#print(raw.text)

html= BeautifulSoup(raw.text, "html.parser")
#print(html)

# 1~3위 컨테이너: div.inner
# 제목: dt.title
# 채널명: dd.chn
# 재생수: span.hit
# 좋아요수: span.like

#1. 컨테이너 수집
container = html.select("div.inner")
#select 함수 이용- div.inner로 선택할 수 있는 모든 데이터 선택- 리스트 형식으로 저장
# 파싱을 했기 때문에 select함수 사용가능- "파싱된 형태에서 div.inner를 골라줘" 라고 명령
##print(container[0]) #1번 데이터 가져올 것이므로 인덱스 0 으로

#2. 영상데이터 수집

for cont in container:
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)


#3. 반복하기
