# openpyxl 연습하기

import openpyexcel

wb = openpyexcel.Workbook() #새로운 워크북을 만들어줘

sheet = wb.active #현재 활성화되어있는 엑셀 파일의 시트

sheet['A1'] = "Hello World" #A1자리에~
sheet.cell(row=3,column=3).value = "Good Bye"

sheet.append(["Python", "Java", "HTML", "JavaScript"])
# append(): 가장 아래에 행별로 데이터를 추가해줌
sheet.append(["Crawling", "DataScience"])

wb.save("test.xlsx")