from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://facebook.com")

input_id = driver.find_element_by_css_selector("input#email")
input_id.send_keys("dotsi")

input_password = driver.find_element_by_css_selector("input#pass")
input_password.send_keys("yoonseo")

# 로그인 버튼 클릭
login = driver.find_element_by_css_selector("input#u_0_e")
login.click()