#1. 컨테이너, 제목, 저자를 선택하는 선택자를 찾아냅니다.
    ## 컨테이너: ul.lst_thum li
    ## 제목: ul.lst_thum li a strong
    ## 저자: ul.lst_thum li a span.writer

#2. 파이썬을 활용해서 데이터 수집기를 만들어냅니다.
#3. (심화)1-20위, 21-40위, ... , 81-100위 서적을 모두 수집할 수 있는 요청값을 찾아 수집기를 만들어 냅니다.

import requests
from bs4 import BeautifulSoup

page=1
for page in range(1,6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(page))
    html = BeautifulSoup(raw.text, "html.parser")

    container = html.select("ul.lst_thum li") #container가 리스트 형태로
    for cont in container:
        title = cont.select_one("ul.lst_thum li a strong").text
        writer = cont.select_one("ul.lst_thum li a span.writer").text

        print(title, writer)

