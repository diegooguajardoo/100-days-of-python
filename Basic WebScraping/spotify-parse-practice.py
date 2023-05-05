from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://kworb.net/spotify/country/global_daily.html")
response.raise_for_status()
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

lst = []
artist_rank_list = []


artists = soup.find_all("td", class_="text mp")
for artist in artists:
	name = artist.get_text()
	lst.append(name)

artist_rank = soup.find_all("td", )
count = 1 
for number in artist_rank:
	ranknumber = number.get_text()
	if count % 11 == 0:
		artist_rank_list.append(ranknumber)
	else:
		pass
	count += 1


print(lst)
print(artist_rank_list)

df = pd.DataFrame(list(zip(lst, pd.to_numeric(artist_rank_list))),columns=['Artist Name', 'Total Streams'])

print(df.sort_values("Total Streams").head(40))
#print(df[df["Change"].str[0] == "+"])

