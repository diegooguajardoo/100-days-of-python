import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movielist = []
allmovies = soup.find_all("h3", class_="title")
for movie in allmovies:
    title = movie.get_text()
    movielist.append(title)
    
movielist = movielist[::-1]

with open("movies.txt", "w") as file:
	for movie in movielist:
		file.write(f"{movie}\n")
	
    
