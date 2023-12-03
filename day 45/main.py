from bs4 import BeautifulSoup
import requests

# with open("index.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# all_of_the_anchor_tag = soup.find_all(name="a")
# # # print(soup.prettify())
# # for tag in all_of_the_anchor_tag:
# #     print(tag.get("href"))
#
# header = soup.find(name="span", class_="down")
# print(header.get_text())

response = requests.get('https://news.ycombinator.com/news')
data = response.text
soup = BeautifulSoup(data, 'html.parser')
articles = soup.find_all(name='a', rel="noreferrer")
article_texts = []
article_links = []
for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
# print(article_texts)
# print(article_links)
# print(article_scores)
list_of_desired_part = []
for text, link, score in zip(article_texts, article_links, article_scores):
    anchor = {
        "text": text,
        "link": link,
        "score": score
    }
    list_of_desired_part.append(anchor)
# for anchor in article_tag:
#     print(anchor)
# max_score = max
max_score = min(list_of_desired_part, key=lambda x: x['score'])
print(max_score)
# for anch in list_of_desired_part:

