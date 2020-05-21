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


# info (장르,감독,배우) dl.lst_dsc dl.info_txt1 dd a
    # 장르 info[0]
    # 감독 info[1]
    # 배우 info[2]

    # select 함수를 이용하는 방법
    info = m.select("dl.info_txt1 dd")

    genre = info[0].select("a")
    director = info[1].select("a")
    actor = info[2].select("a")

    print(title)
    print(star)
    for g in genre: #장르 데이터 여러개일때 있어서- 로맨스, 코미디, ...
        print(g.text)
    for d in director:
        print(d.text)
    for a in actor:
        print(a.text)

    print("="*50)