from selenium import webdriver
import time #파이썬에서 시간을 조정해주는 라이브러리

# 1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")

# 2. 네이버 지도 접속하기
driver.get("https://v4.map.naver.com/") #헤더 필요없음

# 지연시간 주기
time.sleep(1)

# 3. 검색창에 "검색어" 입력하기 //검색창 선택자: input#search-input
search_box = driver.find_element_by_css_selector("input#search-input") #request 보다 더 쉬운 방법으로 찾을 수 있음!
search_box.send_keys("이디야커피") #text를 입력할 수 있는 공간에 이 key를 보내줌 (입력해줌)

# 4. 검색버튼 누르기 // 검색버튼 선택자: button.spm
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()
time.sleep(1) #검색하는 시간 지연 1초

# 5. 검색 결과 확인하기
# 컨테이너: dl.lsnx_det
# 가게 이름: dt > a
# 가게 주소: dd.addr
# 전화번호: dd.tel

# n = 1
for n in range(1, 6):
    container = driver.find_elements_by_css_selector("dl.lsnx_det")
    for cont in container:
        name = cont.find_element_by_css_selector("dt > a").text
        addr = cont.find_element_by_css_selector("dd.addr").text
        #tel = cont.find_element_by_css_selector("dd.tel").text

        print(name, addr)

    # 페이지버튼: div.paginate > *
    page_button = driver.find_elements_by_css_selector("div.paginate > *") # < 1 2 3 ... > 버튼이 리스트 형식으로 저장됨
    page_button[n+1].click()