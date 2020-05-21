# < challenge2 >
# Stage4에서 완성한 네이버 뉴스기사 수집기를 통해 저장되는 엑셀양식에 "검색어"열을 추가합니다.
# 1. 파일의 헤더위치에 "검색어" 카테고리를 추가합니다.
# 2. "검색어" 카테고리에 입력한 키워드를 저장해줍니다.
# *Stage4에서 완성한 수집기 프로그램은 데이터가 누적되어 저장되므로 작동확인을 위해서 기존의 엑셀 파일을 삭제한 후 실행해주셔야합니다.

import requests
from bs4 import BeautifulSoup
import openpyexcel

#keyword = input("검색어: ")
keyword = "코로나"

try: # 일단, week4-7 이란 파일 가져와보고, (없으면 except 실행)
    wb = openpyexcel.load_workbook("navernews_v1.xlsx")
    sheet = wb.active
    print("=== 기존 파일을 불러옵니다 ===")

except: # 엑셀파일 존재하지 않는 경우 여기 실행
    wb = openpyexcel.Workbook()
    sheet = wb.active
    sheet.append(["검색어", "제목", "언론사"]) # 제목|언론사 <--맨 첫 행에 추가
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

        title = title.replace(",", "")
        com = com.replace(",", "") # 제목에 콤마가 포함되는 경우 오류를 피하기위해 콤마를 모두 없애준다.

        sheet.append([keyword, title,com])

wb.save("navernews_v1.xlsx")

