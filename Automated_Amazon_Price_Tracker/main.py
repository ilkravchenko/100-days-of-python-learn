import smtplib
import requests
from bs4 import BeautifulSoup

MY_EMAIL = "bilbob172839@gmail.com"
PASSWORD = "bswxpubchiudxhwi"


URL = 'https://www.amazon.com/Alienware-m15-Gaming-Laptop-15-6-inch/dp/B0B5G3LMZ2/ref=sr_1_15?crid=6KPZAVMVNP5Y&keywords=acer%2Baspire%2Bgaming%2Blaptop&qid=1684401499&sprefix=acer%2Baspire%2Bgamin%2Caps%2C213&sr=8-15&th=1'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept-Language' : 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6'
}

response = requests.get(url=URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, 'html.parser')

name_of_product = soup.find(name='span', id='productTitle').getText().strip()

price = soup.find(name='span', id='price_inside_buybox').getText()
price_without_currency = price.split('$')[1].strip()

if ',' in price_without_currency:
    temp = price_without_currency.split(',')
    price_without_coma = ''.join(temp)

price_float = float(price_without_coma)
#print(price_float)

if price_float < 2200.0:
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n"
                                f"{name_of_product} is now ${price_float}!\n"
                                f"{URL}")