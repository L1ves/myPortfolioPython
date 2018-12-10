import requests
r = requests.get("https://yandex.ru/search/?lr=11168&msid=1514633641.05671.20946.10334&text=sql%20%D0%B4%D0%BB%D1%8F%20%D1%85%D0%B0%D0%BA%D0%B5%D1%80%D0%B0")
print(r)

r.encoding
r.headers
r.text
text = r.text
from bs4 import BeautifulSoup as bs
soup = bs(text, "html.parser")
job = soup('h2')
print(job)
theresult = {}
for fragment in job:
    list_a_tag = fragment.find_all("a")
    for list_a in list_a_tag:
        theresult[list_a.text] = list_a.get("href")
        for key, value in theresult.items():
            theresult[key] = value.replace("/url?q=", "")
theresult
