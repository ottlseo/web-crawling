import requests
from bs4 import BeautifulSoup

for page in range(1,10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=코알라&start="
                   +str(page), headers={"User-Agent":"Mozila/5.0"})
    html = BeautifulSoup(raw.text, "html.parser")
    container = html.select("div.news ul.type01 li")

    for cont in container:
        title = cont.select_one("div.news ul.type01 li dt>a")
        com = cont.select_one("div.news ul.type01 li dd span._sp_each_source")


        print(title.text.strip())
        print(com.text.strip())