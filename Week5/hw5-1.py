# 다음영화 - 예매순위 페이지(http://ticket2.movie.daum.net/Movie/MovieRankList.aspx)에서 영화별 상세페이지에 접속하여
# 영화의 제목 / 장르 / 상영시간(ex, 100분) 데이터를 수집합니다.
# 예매순위 페이지에서 각 영화 상세페이지로 들어갈 수 있는 링크를 찾습니다.
# 상세페이지에서 원하는 데이터(제목, 장르, 누적관객수)를 찾을 수 있는 선택자를 찾습니다.
# 코딩을 통해 데이터 수집기를 완성합니다.
# 데이터를 엑셀에 저장합니다.

# 컨테이너 div.movie_join ul li
# 상세페이지 link = div.movie_join ul li a / link.attr["href"]

# 제목 div.subject_movie strong
# 장르 dl dd.txt_main:nth-of-type(1)


import requests
from bs4 import BeautifulSoup

raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx"
                   , headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, "html.parser")

movies = html.select("div.movie_join ul li") #컨테이너

for m in movies:
    link = m.select_one("div.movie_join ul li a")
    url = link.attrs["href"]

    each_raw = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, "html.parser")

    title = each_html.select_one("div.subject_movie strong").text
    star = each_html.select_one("div.subject_movie em").text
    genre = each_html.select_one("dl dd:nth-of-type(1)").text
    directors = each_html.select("dl dd:nth-of-type(5) a")
    actors = each_html.select("dl dd:nth-of-type(6) a")

    print("제목:", title)
    print("평점:", star)
    print("장르:", genre)

    print("감독:")
    for d in directors:
        print(d.text)

    print("배우:")
    for a in actors:
        print(a.text)
