import requests
import json
query= input("WHAT TYPE OF NEWS YOU WANT?\n")
url= f'https://newsapi.org/v2/everything?q={query}&from=2024-06-14&sortBy=publishedAt&apiKey=3c277ee7177047d9b0fb6624d9b9d284'
r= requests.get(url)
news= json.loads(r.text)
#print(news, type(news))
for article in news['articles']:
    print(article['title'])
    print(article['description'])
    print("...............................................") 