import requests
from bs4 import BeautifulSoup
import openpyexcel

wb = openpyexcel.Workbook()
sheet = wb.active
sheet.append(["제목", "저자"])

for page in range(1, 6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(page),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    books = html.select("div.lst_thum_wrap li")
    for book in books:
        title = book.select_one("a strong").text
        author = book.select_one("span.writer").text

        title = title.replace(",", "")
        author = author.replace(",", "")
        # 콤마가 포함되는 경우 오류를 피하기위해 콤마를 모두 없애준다.

        sheet.append([title, author])

wb.save("naverbook.xlsx")