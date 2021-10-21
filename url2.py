from bs4 import BeautifulSoup
import requests


resultsURL = "https://racerxonline.com/results/2021/salt-lake-city-2/450sx"
praticeURL = "https://motocrossactionmag.com/450-qualifying-results-2021-salt-lake-city-supercross-2/"

##pointsURL = "https://pulpmxfantasy.com/results/saltlakecity2-sx-21/riders"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


resultsPage = requests.get(resultsURL, headers=headers) ##Access racer url
##resultsSoup = BeautifulSoup(resultsPage.content, 'html-parser') ##Pass page url to BeautifulSoup constructor

##table = resultsSoup.find('table') #Finds first table, no idea how to acess other tables on page



## Goal:
## [["Cooper Webb", 1],
##  ["Marvin Musquin", 2]]
##  ......

