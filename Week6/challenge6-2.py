# 구글지도(https://www.google.com/maps/)에 카페를 검색해서 검색된 카페들이 이름, 평점, 주소를 수집합니다.
# 구글지도에서 검색하고 결과를 확인하는 절차를 생각해봅니다.
# 컨테이너, 이름, 평점, 주소를 선택할 수 있는 선택자를 찾습니다.
# 코딩을 통해 데이터를 수집합니다.
# *구글의 경우 지연시간을 길게 주셔야 합니다. (평균 5 ~ 10초)

from selenium import webdriver
import time

# 검색창: input#searchboxinput
# 검색버튼: button#searchbox-searchbutton

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.google.com/maps/")
time.sleep(10)

search_box = driver.find_element_by_css_selector("input#searchboxinput")
search_box.send_keys("이디야커피")

button = driver.find_element_by_css_selector("button#searchbox-searchbutton")
button.click()
time.sleep(10)

# 컨테이너 div.section-result
container = driver.find_elements_by_css_selector("div.section-result")
for cont in container:
    try:
        name = cont.find_element_by_css_selector("div.section-result h3 span").text
    except:
        name = "No name"

    try:
        star = cont.find_element_by_css_selector("div.section-result span.cards-rating-score").text
    except:
        star = "No star"

    try:
        addr = cont.find_element_by_css_selector("div.section-result span.section-result-location").text
    except:
        name = "No address"

# 이름: div.section-result h3 span
# 평점: div.section-result span.cards-rating-score
# 주소: div.section-result span.section-result-location

    print(name, star, addr)

