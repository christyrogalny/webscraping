import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

#https://ebible.org/asv/JHN01.htm

## pick random chapter from the book of John
    ## building the url for this

random_chapter = random.randint(1,21) ## gives random number between 1 and 21 including 1 and 21

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter) ## concatenating two strings
else:
    random_chapter = str(random_chapter) ## for numbers after 10
    ## cannot add to our webpage if its an integer

webpage = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'
print(webpage)


## print all verses from each chapter given from the random above
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read() 

soup = BeautifulSoup(webpage, 'html.parser')

page_verse = soup.findAll("div", attrs={"class":"main"})
#print(page_verse)

for verse in page_verse:
    verse_list = verse.text.split('.') ## spliting based on a period and puts into list
#print(verse_list)

myverse = random.choice(verse_list[:len(verse_list)- 5]) 
    ## give us total number of elements and without the last 5 sentences because we dont need them 
#print(f"Chpater: {random_chapter} , Verse: {myverse}")

message = "Chapter: " + random_chapter + " Verse:" + myverse
print(message)


## Twilio
import keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = "+14245442712"

myCellPhone = "+15616320334"

textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,
                body=message) 

print(textmessage.status) 
