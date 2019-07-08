import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Philips-Trimmer-Cordless-Corded-QT4011/dp/B00JJIDBIC/ref=sr_1_10?crid=TLCV9AZO2YIP&keywords=trimmer+for+mens&qid=1562520254&s=gateway&sprefix=trimm%2Caps%2C280&sr=8-10'

headers = {"User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def f():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # tt = soup.find(id='productTitle')
    # print(tt)
    tt = soup.find(id='productTitle').get_text().strip()
    # print(tt)
    pr = soup.find(id='priceblock_ourprice').get_text()
    dc = pr.index('.')
    pr = pr[1:dc].strip()
    comma = pr.index(',')
    pr = int(pr[:comma] + pr[comma+1:])
    # print(pr)
    if(pr>1500):
        mail()

def mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('snocoder@gmail.com', 'xdezfqcfatqctxfv')
    sub = 'Hurry!, Go and Buy'
    bod = 'Go to the amazon shop'
    msg = f"Subject: {sub}\n\n{bod}"
    server.sendmail(
        'snocoder@gmail.com',
        'adityatripathi087@gmail.com',
        msg
    )
    print('Done!')
    server.quit()

f()