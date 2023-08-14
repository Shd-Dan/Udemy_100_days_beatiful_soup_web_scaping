from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
text_articles = []
link_articles = []

for article in articles:
    article_text = article.getText()
    text_articles.append(article_text)
    article_link = article.a.get("href")
    link_articles.append(article_link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_index = article_upvotes.index(max(article_upvotes))
print(text_articles[highest_index])
print(link_articles[highest_index])

# print(text_articles)
# print(link_articles)
print(article_upvotes)










# import lxml
#
# with open("website.html") as file:
#     data = file.read()
#
# soup = BeautifulSoup(data, "lxml")
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
