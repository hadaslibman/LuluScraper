import requests
from bs4 import BeautifulSoup
import email_sender

class Product:
    def __init__(self, product_link, size_needed, product_description):
        self.product_link = product_link
        self.size_needed = size_needed
        self.product_description = product_description
products = [
    Product(product_link="https://shop.lululemon.com/p/womens-joggers/On-the-Fly-Jogger-Lux/_/prod9610190?color=26950", size_needed=8, product_description="Those red joggers are in!!"),
    Product(product_link="https://shop.lululemon.com/p/womens-joggers/On-the-Fly-Jogger-Lux/_/prod9610190?color=31382", size_needed=4, product_description="Those navy joggers are in!!"),

]
for product in products:
    product_link = product.product_link
    response = requests.get(product_link)
    size_needed = product.size_needed
    product_description = product.product_description

    soup = BeautifulSoup(response.text)
    div = soup.find_all(name="div",attr={"aria-labelledby":"pdp-size-selector-button-tile-group"})

    def send_email():
        email_sender.send_email("Size found " + product_link + "\nDescription: " + product_description)


    for size in soup.find(name="div",class_ = "size-selector").find_all("div", attrs={"role":"radio"}):
       if size.find_all("span")[0].text == str(size_needed):
           send_email()



