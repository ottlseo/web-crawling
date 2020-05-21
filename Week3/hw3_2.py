#네이버뉴스 기사 데이터 수집과 같은 방법으로 다음뉴스 기사 데이터를 1-3페이지까지 수집하는 수집기를 만들어봅니다.
#수집목표: 기사제목/기사 요약
#컨테이너, 기사제목, 기사 요약 선택자 찾기
    #컨테이너: ul#clusterResultUL li
    #기사제목: ul#clusterResultUL li div.wrap_tit
    #기사 요약: ul#clusterResultUL li p
#페이지를 변환하는 요청값 규칙 찾기
    #"&p="+str(page)
#코딩을 통해 데이터 수집기 만들기

import requests
from bs4 import BeautifulSoup

page=1
for page in range(1,4):
    raw = requests.get("https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EC%BD%94%EC%95%8C%EB%9D%BC"
                       "&p="+str(page))
    html = BeautifulSoup(raw.text, "html.parser")

    container = html.select("ul#clusterResultUL li") #container가 리스트 형태로
    for cont in container:
        title = cont.select_one("ul#clusterResultUL li div.wrap_tit").text
        summary = cont.select_one("ul#clusterResultUL li p").text

        print(title, summary)

