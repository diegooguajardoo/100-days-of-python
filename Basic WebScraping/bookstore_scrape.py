import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
productlistnames = []
pricelist = []

allproducts = soup.find_all("h3")
for product in allproducts:
    prodtext = product.get_text()
    productlistnames.append(prodtext)
    
allprices = soup.find_all("p", class_="price_color")
for price in allprices:
    pricenumber = price.get_text()
    pricenumber = float(pricenumber[2:])
    pricelist.append(pricenumber)



df = pd.DataFrame.from_dict({"Products": productlistnames, "Price":pricelist})
df = df.sort_values("Price")

print(df.describe())