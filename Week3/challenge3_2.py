###컨테이너, 순위, 제목 선택자 찾기 - 1주차 자율과제1 참고
#1. 컨테이너: tr.athing
#2. 순위: tr.athing span.rank
#3. 제목: tr.athing td.title > a


###페이지를 변환시키는 URL 요청값 규칙 찾기
#      https://news.ycombinator.com/news?p=2
#       ?p=1,2,3,4,...


###코딩을 통해 수집기 완성하기!!

import requests
from bs4 import BeautifulSoup

page=1;
for page in range(1,4):

    raw = requests.get("https://news.ycombinator.com/news?p="+str(page))
    html = BeautifulSoup(raw.text, "html.parser")

    container = html.select("tr.athing")
    for cont in container:
        rank = cont.select_one("tr.athing span.rank").text
        title = cont.select_one("tr.athing td.title > a").text

        print(rank, title)