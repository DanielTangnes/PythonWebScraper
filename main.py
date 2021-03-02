"""
This code is made to check the price of a product, and send you an email if the price is below a certain value.
im really new to programming and coding, so you probably wanna change some of the code.
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'enter link'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

# checks price of product you set in link. you might have to change some code here, depending on what site you use
def product_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="u-t2 u-word-break").get_text()
    price = soup.find(class_="u-t3").get_text()
    converted_price = int(price[0:2])

    if(converted_price < 30):
        send_mail()

    print(price)
    print(title)

# sends an email to the email address you specified
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sending email address', 'sending email password')

    subject = 'write subject of email'
    body = 'write body of email'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'Sender email address',
        'Recieving email address',
        msg
    )
    print('mail har blitt sendt')
    server.quit()


xc70_price()

while(True):
    xc70_price()
    time.sleep(86400)