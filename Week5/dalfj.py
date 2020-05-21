# 유튜브 메인페이지(https://www.youtube.com/)에서 자신의 맞춤동영상 목록의
# 영상제목 / 크리에이터 데이터를 수집합니다.
# 크리에이터 정보 상세페이지로 들어갈 수 있는 링크를 찾습니다.
# 상세페이지에서 "구독자 수"를 찾을 수 있는 선택자를 찾습니다.
# 코딩을 통해 데이터 수집기를 완성합니다.
# 엑셀에 저장

# 컨테이너 ytd-rich-item-renderer.ytd-rich-grid-renderer

# 제목 ytd-rich-item-renderer.ytd-rich-grid-renderer h3 a
# 크리에이터 ytd-rich-item-renderer.ytd-rich-grid-renderer yt-formatted-string#text

# 상세페이지
# 구독자수

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.youtube.com/"
                   , headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, "html.parser")

container = html.select("ytd-rich-item-renderer.ytd-rich-grid-renderer") #컨테이너

for c in container:
    title = c.select_one("ytd-rich-item-renderer.ytd-rich-grid-renderer h3 a").text
    creator = c.select_one("ytd-rich-item-renderer.ytd-rich-grid-renderer yt-formatted-string#text")


    #each_raw = requests.get("https://www.youtube.com/"+url, headers={"User-Agent":"Mozilla/5.0"})
    #each_html = BeautifulSoup(each_raw.text, "html.parser")

    #day = each_html.select_one()



    print("https://www.youtube.com/"+url)