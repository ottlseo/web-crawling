import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn"
                   , headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, "html.parser")

# 컨테이너> dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    title = m.select_one("dl.lst_dsc dt.tit a").text.strip()
    star = m.select_one("dl.lst_dsc div.star_t1 a span.num").text.strip()

    # 영화제목 dl.lst_dsc dt.tit a
    # 평점 dl.lst_dsc div.star_t1 a span.num

# 선택자 이용한 방법
    # 장르 dl.info_txt1 dd:nth-of-type(1) a
    # 감독 dl.info_txt1 dd:nth-of-type(2) a
    # 배우 dl.info_txt1 dd:nth-of-type(3) a

    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    director = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    actor = m.select("dl.info_txt1 dd:nth-of-type(3) a")

    print(title)
    print(star)
    for g in genre: #장르 데이터 여러개일때 있어서- 로맨스, 코미디, ...
        print(g.text)
    for d in director:
        print(d.text)
    for a in actor:
        print(a.text)

    print("="*50)