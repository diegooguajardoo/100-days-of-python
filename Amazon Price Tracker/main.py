import requests
import pprint
from bs4 import BeautifulSoup
import lxml
import time

def get_price():
	pp = pprint.PrettyPrinter()
	product_link = "https://www.amazon.com/-/es/38GN95B-B-UltragearTM-actualizaci%C3%B3n-DisplayHDRTM-compatibilidad/dp/B08CQSQSH9/ref=sr_1_5?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2HQK80MHRTXTC&keywords=monitor&qid=1683127322&refinements=p_n_feature_fifteen_browse-bin%3A17751805011&rnid=17751799011&s=pc&sprefix=monitor%2Caps%2C198&sr=1-5"

	r = requests.get(url=product_link,
	                 headers={
	                     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0", 
	                     "Accept-Language": "en-US,en;q=0.5"
	                     })

	text = r.content
	soup = BeautifulSoup(text,"lxml")
	spans = soup.find(class_="a-offscreen").get_text()[3:].replace(",","")
	priceasfloat = float(spans)
	return priceasfloat


time.sleep(30)
print(get_price())

