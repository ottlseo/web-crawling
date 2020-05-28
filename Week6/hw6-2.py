# 인스타그램에서 ootd 해시태그 검색결과(https://www.instagram.com/explore/tags/ootd/) 페이지에 접속해서 12개 포스트의 본문 내용을 수집합니다.
# 본문 데이터 수집을 수집을 위한 절차를 생각해봅니다.
# 선택자와 지연시기를 생각해봅니다.
# 코딩을 통해 본문 수집기를 완성합니다.

from selenium import webdriver
import time
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.instagram.com/explore/tags/ootd/")

login_close = driver.find_element_by_css_selector("button.dCJp8")
login_close.click()

instagram = driver.find_elements_by_css_selector("div.v1Nh3")
instagram = instagram[:12]

# 컨테이너 반복하기
for insta in instagram:
    insta.click()

    time.sleep(1)
    post = driver.find_element_by_css_selector("div.C4VMK span").text
    print(post)

    but_close = driver.find_element_by_css_selector("button.ckWGn")
    but_close.click()
