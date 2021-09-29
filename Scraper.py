
from bs4 import BeautifulSoup
import requests

url = "https://www.realmeye.com/player/Savoror"

##Required to bypass 403 forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser') #Pass page content to BeautifulSoup constructor

table = soup.find('table') #Finds first table, no idea how to acess other tables on page

table_rows = table.find_all('tr') # Find table rows

for tr in table_rows:
    td = tr.find_all('td') # 'td' - table data cells
    row = [i.text for i in td]
    print(row)


##print(soup.find_all(string=["Knight", "Huntress", "Priest"]))
##print(soup.prettify()) //Readable text

 