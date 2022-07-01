import requests
from bs4 import BeautifulSoup

Url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(Url).content

Soup = BeautifulSoup(html, "html.parser")

Liste = Soup.find_all("li", {"class":"column"}, limit=5)

for x in Liste:
    name = x.div.a.h3.text.strip()
    link = x.div.a.get("href")
    oldprice = x.find("div", {"class":"priceContainer"}).find_all("span")[0].text.strip().strip("TL")
    newprice = x.find("div", {"class":"priceContainer"}).find_all("span")[1].text.strip().strip("TL")
    rating = x.find("div", {"class":"proDetail"}).find_all("span")[1].text.strip()
    print(f"""
    
    Bilgisayar : {name}  
    Link : {link}     
    İndirimsiz Fiyat : {oldprice} TL
    İndirimli Fiyat : {newprice}  TL
    Rating : {rating}
    """)
