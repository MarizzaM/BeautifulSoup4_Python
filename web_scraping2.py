from bs4 import BeautifulSoup
import re


with open("index2.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

# result = doc.find("option")
# result = doc.find_all("option")
# print(result)

# tag = doc.find("option")
# print(tag.attrs)
# tag['selected'] = 'false'
# tag['color'] = "blue"
# print(tag)

# tags = doc.find_all(["p", "div", "li"])
# tags = doc.find_all(["option"], text="Undergraduate")

# tags = doc.find_all(["option"], text="Undergraduate", value="undergraduate")

# tags = doc.find_all(class_="btn-item")

# tags = doc.find_all(text=re.compile("\$.*"))

# tags = doc.find_all(text=re.compile("\$.*"), limit=1)
# for tag in tags:
# 	print(tag.strip())


tags = doc.find_all("input", type="text")
for tag in tags:
	tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
	file.write(str(doc))