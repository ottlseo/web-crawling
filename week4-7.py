# 엑셀 심화: 상황에 따라 다르게 쓰기

import requests
from bs4 import BeautifulSoup
import openpyexcel

keyword = input("검색어: ")

try: # 일단, week4-7 이란 파일 가져와보고, 없으면
    wb = openpyexcel.load_workbook("week4-7.xlsx")
    #.load_workbook("<엑셀파일명>")
# 단점!!! week4-7.xlsx 파일이 없는 경우 에러 -이므로 try 사용
    sheet = wb.active

except: # 엑셀파일 존재하지 않는 경우 여기 실행
    wb = openpyexcel.Workbook()
    sheet = wb.active
    sheet.append(["제목", "언론사"]) # 제목|언론사 <--맨 첫 행에 추가
    print("=== 새로운 파일이 생성되었습니다 ===")

for page in range(1,100,10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
                       +keyword+"&start="+str(page), headers={"User-Agent":"Mozila/5.0"})
    html = BeautifulSoup(raw.text, "html.parser")

    container = html.select("div.news ul.type01 > li")

    for cont in container:
        title = cont.select_one("div.news ul.type01 > li a._sp_each_title").text
        com = cont.select_one("div.news ul.type01 > li dd span._sp_each_source").text
        print(title, com)

        # 제목에 콤마가 포함되는 경우 오류를 피하기위해 콤마를 모두 없애준다.
        title = title.replace(",", "")
        com = com.replace(",", "")

        sheet.append([title,com])


wb.save("test4-7.xlsx")

