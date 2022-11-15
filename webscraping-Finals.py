from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

url = 'https://registrar.web.baylor.edu/exams-grading/fall-2022-final-exam-schedule' 
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read() 

soup = BeautifulSoup(webpage, 'html.parser')


tables = soup.findAll('table') ## looking for table tag so you only get whats in the second table (see code)
## used 'table' because we wanted to skip the first table and only use the second

finals_table = tables[1] 

#print(finals_table)

all_rows = finals_table.findAll('tr') ## find all rows in finals table - looking for tr tag 

myclasses_file = open('classes.csv', 'r')
myclasses = csv.reader(myclasses_file,delimiter=',')
next(myclasses) ## skips header on csv file

for rec in myclasses: 
    day = rec[0] ## this is taking information from csv file
    time = rec[1]

    for row in all_rows:
        cell = row.findAll('td')
        if cell: ## adding this if statement will get rid on the first row which only contains [] (empty brackets)
            sch_day = cell[0].text ## this is taking information from the website 
            sch_time = cell[1].text 
            exam_day = cell[2].text
            exam_time = cell[3].text

            if sch_day == day and sch_time == time:
                print(f"Class day and time: {day} - {time} ")
                print(f"Exam Day and Time: {exam_day} - {exam_time}")
                print()
                print()
