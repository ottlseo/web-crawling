import requests
from bs4 import BeautifulSoup

# Challenge1
# 4~10위 컨테이너:
# 제목/채널명/조회수/좋아요수 반복문으로 출력

raw = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(raw.text, "html.parser")


#컨테이너: div.cds

#제목: div.cds dt.title > a
#채널명: div.cds dd.chn > a
#재생수: div.cds span.hit
#좋아요수: div.cds span.like

container = html.select("div.cds") #container변수에 컨테이너(4~10)가 리스트 형태로 저장됨

for cont in container:
    title= cont.select_one("div.cds dt.title")
    chn = cont.select_one("div.cds dd.chn")
    hit = cont.select_one("div.cds span.hit")
    like = cont.select_one("div.cds span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)
