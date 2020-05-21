# 다음뉴스 기사 데이터(기사제목/기사요약)를
# 1-3페이지까지 수집하여 원하는 방식으로 저장합니다. (csv, xlsx)
import requests
from bs4 import BeautifulSoup
import openpyexcel

wb = openpyexcel.Workbook()
sheet = wb.active
sheet.append(["기사 제목", "기사 요약"])

for page in range(1, 4):
    raw = requests.get("https://search.daum.net/search?w=news&q=코알라&p="+str(page))
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.wrap_cont")

    for ar in articles:
        title = ar.select_one("a.f_link_b").text
        summary = ar.select_one("p.f_eb.desc").text

        sheet.append([title,summary])

wb.save("daumnews.xlsx")