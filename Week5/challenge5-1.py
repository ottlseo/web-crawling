# IMDb(https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd)
# 현재 상영중 영화목록에서 상영 중인 영화의 제목 /  감독 / 배우 데이터를 수집합니다.

# 컨테이너, 제목, 감독, 배우 데이터를 선택할 수 있는 선택자를 찾습니다.
# 파이썬을 통해 데이터를 수집할 수 있는 데이터 수집기를 만듭니다.
# (심화) 조건문을 활용하여 Action 장르의 영화만 출력합니다.

    #컨테이너 > div.mode-detail
    #제목 > div.mode-detail h3.lister-item-header a
    #감독+배우 > div.mode-detail p:nth-of-type(3) a

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd")
html = BeautifulSoup(raw.text, "html.parser")
movies = html.select("div.mode-detail")

for m in movies:
    title = m.select_one("div.mode-detail h3.lister-item-header a").text
    people = m.select("div.mode-detail p:nth-of-type(3)")
    #people = people.text.replace("Directors:", "").replace("Stars:", "")
    #어떤게 리스트인지 아닌지가 정리가 안 돼서 오류가 난 것 같습니다.
    ## 수정- 감독이 없는 경우도 있어서 오류-> for문 사용하여 수정하기 V
    directors = people.text.split("|")[0]
    stars = people.text.split("|")[1]

    print("< Title >")
    print(title)
    print("< Directors >")
    for d in directors:
        print(d.strip())
    print("< Stars >")
    for s in stars:
        print(s.strip())
