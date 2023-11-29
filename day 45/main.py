from bs4 import BeautifulSoup
with open("index.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
all_of_the_anchor_tag = soup.find_all(name="a")
# # print(soup.prettify())
# for tag in all_of_the_anchor_tag:
#     print(tag.get("href"))

header = soup.find(name="span")
print(header)

