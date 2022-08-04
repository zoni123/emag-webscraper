import requests
from bs4 import BeautifulSoup
x = input("Search: ")
URL = "https://www.emag.ro/search/" + x
page = requests.get(URL)
content = BeautifulSoup(page.content, "html.parser")
results = content.find(id="card_grid")
info = results.find_all("div", class_="card-v2")
print("\n---RESULTS---\n")
for result in info:
    name = result.find("a", class_="card-v2-title semibold mrg-btm-xxs js-product-url")
    av = result.find("div", class_="card-estimate-placeholder")
    price = result.find("p", class_="product-new-price")
    article = result.find("a")["href"]
    print(name.text)
    print(av.text)
    print(price.text)
    print("ARTICLE: " + article)
    print("\n")
