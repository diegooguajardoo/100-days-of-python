import requests
from bs4 import BeautifulSoup

date = input(
    "Which year do you want to travel to? Type the date in this format YYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status()
response = response.text
soup = BeautifulSoup(response, "html.parser")
chart = soup.find_all("div", class_="o-chart-results-list-row-container")
list100 = []
artists100 = []

for i in chart:
    i = i.find("h3", class_="c-title")
    song = i.get_text()
    song = song.strip().replace("\n", "")
    song = song.strip().replace("\t", "")
    list100.append(song)

for i in chart:
    i = i.find("span", class_="c-label")
    artist = i.get_text()
    artists100.append(artist)

print(list100)
print(artists100)
