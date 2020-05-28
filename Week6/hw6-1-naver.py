# Selenium을 활용하여 네이버 로그인 페이지(https://nid.naver.com)와 페이스북(https://www.facebook.com)에 자동으로 로그인하는 프로그램을 만들어 봅니다.
# 로그인 절차에 대해 생각해봅니다.
# 아이디/비밀번호를 입력하고 로그인버튼을 누를 수 있는 선택자를 찾습니다.
# 코딩을 통해 자동 로그인 장치를 만들어봅니다.

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://nid.naver.com")

input_id = driver.find_element_by_css_selector("input#id")
input_id.send_keys("dotsi")

input_password = driver.find_element_by_css_selector("input#pw")
input_password.send_keys("yoonseo")

# 로그인 버튼 클릭
button = driver.find_element_by_css_selector("input.btn_global")
button.click()