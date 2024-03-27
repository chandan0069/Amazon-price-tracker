
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

url = 'https://www.amazon.in/Souled-Store-Official-Rebel-Moon/dp/B0CTHMMJTG/ref=sr_1_5?dib=eyJ2IjoiMSJ9.BYgObAMh-ziI2-vLRwkXt1851CXrQxzQBnnljaFEyaS7ZhlZK4blnaeHooJNSuvM87PtVhHtfa5gQ0G8ok8L4-RjPh84oEpHOeBAHbV-Z9aA_iybwb7v8CpHWQ-utOY1U3g7wq0nUg6E-f39h54d3bJzCnMrFnJvUTIByRTdO29hq7J2CXKQNfq5UJBcruEkRJR_AXysjEA3nlGyX9LxZOx2iDuSonH37It1qn-9Z6Qqp_EZSJTEROyUqdnt8uzPehHyvv4U6HToxhWysOnUUeDKhWTHon5Aa6G8pfg9vsw.a-6-Fetq-nzEyRQBgSS8UoDLkeSjEw2GW3iYJQQm0Q8&dib_tag=se&pf_rd_i=1968024031&pf_rd_m=A1K21FY43GMZF8%2CA1VBAL9TL5WCBF%2CA1VBAL9TL5WCBF&pf_rd_p=20267dca-5026-4de3-b05c-4b9531fe1b71&pf_rd_r=5M0P4RT4M26WXG4HCT55%2C8JKP1TYMBNZ7T7X8DBK7%2CXWN8YCMEDN9M3VX5X2SD&pf_rd_s=merchandised-search-16&pf_rd_t=101%2C30901&qid=1711558605&refinements=p_85%3A10440599031%2Cp_n_pct-off-with-tax%3A0-%2Cp_89%3AThe%2BSouled%2BStore%2Cp_36%3A39900-&rnid=4595083031&rps=1&s=apparel&sr=1-5&th=1&psc=1'
headers = {
    "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')

response = requests.get(url, headers=headers)

# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
soup.prettify()
# print(soup)

item_price = float(soup.find(class_='a-price-whole').getText())
# print(item_price)

msg_content = f"Subject:Amazon Price Alert!\n\nThe Souled Store Official Rebel Moon: Galactic Short Sleeve Round Neck Brown Graphic Print Oversized Fit T-Shirt is now ₹{item_price}\nhttps://www.amazon.in/Souled-Store-Official-Rebel-Moon/dp/B0CTHMMJTG/".encode("utf-8")
BUY_PRICE = 500

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    if item_price < BUY_PRICE:
        connection.sendmail(to_addrs=MY_EMAIL, from_addr=MY_EMAIL, msg=msg_content)