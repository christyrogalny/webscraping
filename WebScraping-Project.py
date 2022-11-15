# Find a 'scrappable' cryptocurrencies website where you can scrape 
# the top 5 cryptocurrencies and display as a formatted output one 
# currency at a time. The output should display the name of the currency, 
# the symbol (if applicable), the current price and % change in the last 24 hrs 
# and corresponding price (based on % change)

# Furthermore, for Bitcoin and Ethereum, the program should alert you via text 
# if the value falls below $40,000 for BTC and $3,000 for ETH.

# 'https://www.coingecko.com/' 


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://www.coingecko.com/' 

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read() 

soup = BeautifulSoup(webpage, 'html.parser')


table = soup.findAll("td")

s1 = ","
s2 = "$"
s3 = "%"
s4 = ""

name = 2
current_price = 3
percent_change = 5
count = 1

for x in range(5): 
    company = table[name].text.split()
    print(f"Name: {company[0]}")
    print(f"Current Price: {table[current_price].text.strip()}")
    print(f"Percent Change: {table[percent_change].text.strip()}")

    calc_price = (float(table[current_price].text.strip().replace(s1,s4).replace(s2,s4)) * 
                    (1 - float(table[percent_change].text.strip().replace(s3,s4)) / 100))

    print("Corresponding Price: ${:,.2f}".format(calc_price))
    print()

    name += 12
    current_price += 12
    percent_change += 12



btc_value = (table[3].text.strip().replace(s1,s4).replace(s2,s4))
eth_value = (table[15].text.strip().replace(s1,s4).replace(s2,s4))
new_btc = float(btc_value)
new_eth = float(eth_value)


import keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = "+14245442712"

myCellPhone = "+15616320334"

btc_message = "The value for Bitcoin is now " + table[3].text.strip()
eth_message = "The value for Ethereum is now " + table[15].text.strip()


if new_btc < 40000:
    text1 = client.messages.create(to=myCellPhone,from_=TwilioNumber, body=btc_message) 
if new_eth < 3000:
    text2 = client.messages.create(to=myCellPhone,from_=TwilioNumber, body=eth_message) 

