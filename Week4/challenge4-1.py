import requests
from bs4 import BeautifulSoup

# csv 형식으로 저장하기
f = open("navernews2.csv", "w", encoding="UTF-8")
f.write("기사 제목, 언론사\n")  # 수집한 데이터가 어떤 데이터인지 헤더를 넣어주는 작업 중요

for page in range(1,100,10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=코알라&start="
                   +str(page), headers={"User-Agent":"Mozila/5.0"})
    html = BeautifulSoup(raw.text, "html.parser")

    container = html.select("div.news ul.type01 > li")

    for cont in container:
        title = cont.select_one("div.news ul.type01 > li a._sp_each_title").text
        com = cont.select_one("div.news ul.type01 > li dd span._sp_each_source").text
        print(title, com)

        # 제목에 콤마가 포함되는 경우 오류를 피하기위해 콤마를 모두 없애준다.
        title = title.replace(",", "")
        com = com.replace(",", "")
        f.write(title + ',' + com + '\n')

f.close()
