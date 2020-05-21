# 제목: div.mode-detail h3 a

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

raw = requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd",
                            headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, "html.parser")

movies = html.select("div.mode-detail") #컨테이너

for m in movies:
    title = m.select_one("div.mode-detail h3.lister-item-header a")
    url = title.attrs["href"] #title 태그의 속성- href 태그의 값(url)을 저장

    each_raw = requests.get("https://www.imdb.com"+url,
                            headers={"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, "html.parser")

    poster = each_html.select_one("div.poster img")
    poster_url = poster.attrs["src"]


    urlretrieve(poster_url, "poster_for5-2/"+title.text[:2]+".png")
        # poster_for5-2 폴더 안에, 제목 처음 두글자로 포스터(.png) 저장
