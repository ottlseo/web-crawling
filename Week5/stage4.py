import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

raw = requests.get("https://movie.naver.com/movie/running/current.nhn"
                   , headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, "html.parser")

# 컨테이너> dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    title = m.select_one("dl.lst_dsc dt.tit a")
    url = title.attrs["href"]
    print("<",title.text,">")
    each_raw = requests.get("https://movie.naver.com"+url,
                            headers={"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, "html.parser")

    poster = each_html.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]
    # print(poster_src)


    urlretrieve(poster_src, "poster/"+title.text[:2]+".png")
    # poster 폴더 안에, 앞에 두 글자로 사진 저장

# /movie/bi/mi/basic.nhn?code=193804
# https://movie.naver.com/movie/bi/mi/basic.nhn?code=193804

# 포스터: https://movie-phinf.pstatic.net/20200428_196/1588038709486FYyHu_JPEG/movie_image.jpg?type=m203_290_2

