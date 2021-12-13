from bs4 import BeautifulSoup
import requests

# HTML From File
# with open("index.html", "r") as f:
# 	doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify())

# tag = doc.title
# tag.string = 'hello'

# print(tag)
# print(doc.prettify())

# tags = doc.find_all('p')[0].get_text()
# print(tags)


# HTML From Website
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# print(doc.prettify())

prices = doc.find_all(text="$")

# print(prices)

parent = prices[0].parent

# print(parent.prettify())

strong = parent.find("strong")
print(strong.string)