import requests
from openpyxl import Workbook
from openpyxl.styles import Font
from bs4 import BeautifulSoup

if __name__ == '__main__':
    output = Workbook()
    output_page = output.active
    output_page.column_dimensions['A'].width = 5
    output_page.column_dimensions['B'].width = 100
    output_page.column_dimensions['C'].width = 25
    output_page.column_dimensions['D'].width = 15
    output_page.column_dimensions['E'].width = 10
    output_page.column_dimensions['F'].width = 20
    i = 1
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
        review = result.find("span", class_="average-rating semibold")
        review_n = result.find("span", class_="visible-xs-inline-block")
        article = result.find("a")["href"]
        print(str(i) + ". " + name.text)
        output_page['A' + str(i)] = str(i)
        output_page['A' + str(i)].font = Font(bold=True)
        output_page['B' + str(i)] = name.text
        print(av.text)
        output_page['C' + str(i)] = av.text
        print(price.text)
        output_page['D' + str(i)] = price.text
        if review is not None:
            if review_n.text == "(1)":
                print("Rating: " + review.text + "/5 -> (1) review")
                output_page['E' + str(i)] = review.text + "/5"
                output_page['F' + str(i)] = "(1) review"
            else:
                print("Rating: " + review.text + "/5 -> " + review_n.text + " reviews")
                output_page['E' + str(i)] = review.text + "/5"
                output_page['F' + str(i)] = review_n.text + "reviews"
        else:
            print("No reviews yet")
            output_page['E' + str(i)] = '-'
        print("ARTICLE: " + article)
        print("\n")
        i += 1
    output.save("output.xlsx")
