# Selenium을 사용해서 파파고(https://papago.naver.com)에서 "seize the day"라는 문장을 입력, 번역결과를 출력하는 프로그램을 만들어봅니다.
# 파파고 번역 서비스 이용 절차를 적어봅니다.
# 지연시간이 필요한 부분을 생각해봅니다.
# 코딩을 통해 번역결과를 출력합니다.

from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://papago.naver.com/")

time.sleep(1) #지연시간 1초

# 번역할 내용 입력: textarea#txtSource
txt = driver.find_element_by_css_selector("textarea#txtSource")
txt.send_keys("Seize the day")

# 버튼: button#btnTranslate
button = driver.find_element_by_css_selector("button#btnTranslate")
button.click()

time.sleep(1) #지연시간 1초
translate = driver.find_element_by_css_selector("div#txtTarget span").text
print(translate)

driver.close()

