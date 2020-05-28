# requests 로 수집할 수 없는 페이지 = 동적 페이지
# 동적페이지는 URL이 바뀌지 않아서 selenium 이라는 패키지가 필요함
# selenium 연습하기
from selenium import webdriver
import time #파이썬에서 시간을 조정해주는 라이브러리

# (셀레니움은 직접 웹드라이버를 열어서 데이터를 검색하고 수집하기 때문에,
# 우리가 어떤 경로로 하는지 꼭 알아야함)

# 1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")

# 2. 네이버 지도 접속하기
driver.get("https://v4.map.naver.com/") #헤더 필요없음

time.sleep(1)  #  지연시간 1초

# 3. 검색창에 "검색어" 입력하기 //검색창 선택자: input#search-input
search_box = driver.find_element_by_css_selector("input#search-input") #request 보다 더 쉬운 방법으로 찾을 수 있음!
search_box.send_keys("이디야커피") #text를 입력할 수 있는 공간에 이 key를 보내줌 (입력해줌)
time.sleep(1)

# 4. 검색버튼 누르기 // 검색버튼 선택자: button.spm
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click() #클릭해줘

# 5. 검색 결과 확인하기
# 컨테이너: dl.lsnx_det
# 가게 이름: dt > a
# 가게 주소: dd.addr
# 전화번호: dd.tel

# 기존 requests에서 했던 방식: stores = html.select("") //컨테이너
# selenium에서도 같은 방식! 바꿀건 html->driver, select()->find_elements_by_css_selector()

stores = driver.find_elements_by_css_selector("dl.lsnx_det")
for s in stores:
    name = s.find_element_by_css_selector("dt > a").text
    addr = s.find_element_by_css_selector("dd.addr").text
    tel = s.find_element_by_css_selector("dd.tel").text

    print(name)
    print(addr)
    print(tel)