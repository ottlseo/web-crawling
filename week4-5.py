import requests
from bs4 import BeautifulSoup
import openpyexcel

wb = openpyexcel.Workbook()
sheet = wb.active
sheet.append(["제목", "채널명", "재생수", "좋아요수"])

raw = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(raw.text, "html.parser")
container = html.select("div.inner")

for cont in container:
    title = cont.select_one("dt.title").text.strip()
    chn = cont.select_one("dd.chn").text.strip()
    hit = cont.select_one("span.hit").text.strip()
    like = cont.select_one("span.like").text.strip()

    # 제목에 콤마가 포함되는 경우 오류를 피하기위해 콤마를 모두 없애준다.
    title = title.replace(",", "")
    chn = chn.replace(",", "")
    hit = hit.replace(",", "")
    like = like.replace(",", "")

    hit = hit.replace("재생 수", "")
    like = like[5:]

    sheet.append([title, chn, hit, like])

    # print(title.text.strip())
    # print(chn.text.strip())
    # print(hit.text.strip())
    # print(like.text.strip())
    # print("="*50)

wb.save("test4-5.xlsx")