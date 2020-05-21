import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn"
                   , headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, "html.parser")

# 컨테이너> dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    title = m.select_one("dl.lst_dsc dt.tit a")
    url = title.attrs["href"]  # /movie/bi/mi/basic.nhn?code=193804
    print("<",title.text,">")
    each_raw = requests.get("https://movie.naver.com"+url,
                            headers={"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, "html.parser")

    review = each_html.select("div.score_result ul li") #이동한 url에서 얻어올 컨테이너
    for r in review:
        star = r.select_one("div.score_result ul li div.star_score em") #평점
        reple = r.select_one("div.score_result ul li div.score_reple p") #리플

        print(star.text.strip(), reple.text.strip())
    print("="*50)


# /movie/bi/mi/basic.nhn?code=193804
# https://movie.naver.com/movie/bi/mi/basic.nhn?code=193804

