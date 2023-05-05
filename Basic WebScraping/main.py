from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")

titles = soup.find("span", class_="titleline")
article_text = titles.get_text()
print(article_text)

article_link = titles.get("href")
print(titles)
	
