import requests
import json
query = input("What type of input are you interested in: ")

url = f"https://www.googleapis.com/customsearch/v1?key=AIzaSyB0_m6OE19epA7LcE_Ib5xeayxak8gw7Tg&cx=017576662512468239146:omuauf_lfve&q={query}"

r = requests.get(url)
news = json.loads(r.text)

print(news,type(news))
