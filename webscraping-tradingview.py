from unicodedata import name
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'http://www.webull.com/quote/us/gainers' 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
## allows us to make a request to that website giving the header so it knows the user agent

webpage = urlopen(req).read() 

soup = BeautifulSoup(webpage, 'html.parser')
## feeding this information into beautiful soup then parser it (parser: breaks things up/separates things like a comma)

title = soup.title

print(title.text)



#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

tablecells = soup.findAll("div", attrs={"class":"table-cell"})

print(tablecells[0].text) 
    ## setting the index to 0 shows only the first index in the list
    ## which makes it easier to read 
    ## print(tablecells[0]) prints: 
        ## <div class="table-cell" style="flex:0 0 28px;text-align:left"><span class="ssr7219826 ssr7219827">1</span></div>
    ## print(tablecells[0].text) 
        ## prints: 1


##print out company name, change, high, low
#print(tablecells[1].text +"\n"+ tablecells[3].text +"\n"+ tablecells[5].text +"\n"+ tablecells[6].text)
print(tablecells[1].text) #name
print(tablecells[3].text) #change
print(tablecells[5].text) #high
print(tablecells[6].text) #low


## grab info for top 5 companies and calculate percentage change 
## percentage change calculation:
        ## high - low = value
        ## value/low * 100 = % change
name = 1
high = 5 ## high is the 5th in the table
low = 6
count = 1

while count <= 5:
    calc = ((float(tablecells[high].text) - float(tablecells[low].text))) * 100 
    print(f'Name:{tablecells[name].text} || High: {tablecells[high].text} || Low: {tablecells[low].text}')
    print(calc)
    name += 11
    high += 11
    low += 11
    count += 1
    ## 11 is on the second row


## can also be done like this
## this is how prof did it
tablecells = soup.findAll("div", attrs={"class":"table-cell"})
counter = 1

for x in range(5):
    name = tablecells[counter].text
    change = tablecells[counter+2].text ## +2 is where the cell is in the table 
    high = float(tablecells[counter+4].text)
    low = float(tablecells[counter+5].text)

    calc_change = round(((high - low) / low) * 100, 2)

    print(name)
    print(f"Changed %: {change}")
    print(f"High: {high}")
    print(f"Low: {low}")
    print(f"Calculated change: {calc_change}%")
    print()
    print()

    counter += 11 ## use 11 because we start with counter equal to 1, and 11 starts the second row 
