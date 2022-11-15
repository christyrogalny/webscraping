
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font

#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
##
##
##
##

## top 5: 
## rank
## movie name
## total gross
## distributor
## average gross per theater = total gross / number of theaters

s1 = ","
s2 = "$"
s4 = ""

table = soup.findAll("td")
rank = 0 
name = 1 
total_gross = 7 
distributor = 9  
num_theaters = 6 


for x in range(5):
    print(f"Rank: {table[rank].text}")
    print(f"Movie Name: {table[name].text}")
    print(f"Total Gross: {table[total_gross].text}")
    print(f"Distributor: {table[distributor].text.strip()}")

    avg_gross = round(float(table[total_gross].text.replace(s1,s4).replace(s2,s4)) / 
                        float(table[num_theaters].text.replace(s1,s4)),2)

    print("Average Gross: ${:,.2f}".format(avg_gross))
    print()

    rank += 11
    name += 11
    total_gross += 11
    distributor += 11
    num_theaters += 11
    