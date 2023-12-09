import smtplib
import requests
from pprint import pprint
from bs4 import BeautifulSoup

buy_price = 500

product_link = "https://www.amazon.com/Google-Pixel-Unlocked-Smartphone-Advanced/dp/B0CGT6RLT7?ref_=Oct_DLandingS_D_cf754241_2&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url=product_link, headers=header)
data = response.content

soup = BeautifulSoup(data, 'html.parser')
title = soup.find(id="productTitle").get_text().strip()
price = soup.find(class_="a-offscreen").get_text()
price = float(price.split("$")[1])
print(price)
if price <= buy_price:
    message = f"{title} is now at {price}"
    with smtplib.SMTP(your_smtp_address, port=587) as connection:
        connection.starttls()
        result = connection.login(your_email, your_password)
        connection.sendmail(
            from_addr=your_email,
            to_addrs=your_email,
            msg=message.encode("utf-8")
        )