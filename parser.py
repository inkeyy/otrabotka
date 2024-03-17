import requests
from bs4 import BeautifulSoup

url = 'https://dedmorozural.ru/'
responce = requests.get(url)
print(responce.status_code)
# print(responce.text)

soup = BeautifulSoup(responce.text, "html.parser")
# print(soup.title)
# print(type(soup))
print(soup.a.get("href"))

a_tags = soup.find_all("a")
for a_tags in a_tags:
    print(a_tags)

big_body_div = soup.find(name= 'div', class_ = 'modulebody1')

print(big_body_div)



