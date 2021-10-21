from bs4 import BeautifulSoup
import requests


# Practice Result URLs
praticeURL = "https://motocrossactionmag.com/450-qualifying-results-2021-salt-lake-city-supercross-2/"

# Point Result URLs
##pointsURL = "https://pulpmxfantasy.com/results/saltlakecity2-sx-21/riders"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


def readContents (url):
    resultsPage = requests.get(url, headers = headers) ##Access racer url
    resultsSoup = BeautifulSoup(resultsPage.content, 'html.parser') ##Pass page url to BeautifulSoup constructor
    table = resultsSoup.find('table') #Finds first table, no idea how to acess other tables on page

    return table 


def toTable (content):

    ##Read to Table
    table_rows = content.find_all('tr')
    
    inter = []

    # Get all rows of table 
    for tr in table_rows:
        td = tr.find_all('td') # 'td' - table data cells
        row = [i.text for i in td]
        inter.append(row)
    
    
    inter.remove([]) ##Empty list ()/._.)/


    ##Clean table data
    pos = 0
    rName = 1
    raceResults = []
    for result in inter:

        # append rider names
        raceResults.append(result[rName])
        
        # append list of race results 
        r = int(result[pos])
        raceResults.append( [r] )
    
    return raceResults


def combineTable (temp, final):

    # [RiderName, [Int]]

    index = 0
    for rider in temp:

        ## Append to existing rider 

        if rider in final and index % 2 == 0:  ##rider in final and index % 2 == 0:
            print(rider)
            #final.append(r)

        elif rider not in final and index % 2 == 0:
            print("Elif Statement: ",rider, "    Index: ", index, "       Possible results???  ", temp[index + 1])
            final.append(rider)

            result = temp[index + 1][0]
            #result = int(result)
            final.append([result])



        index +=1

    
    return final





## Driver code ##


urls = ["https://racerxonline.com/results/2021/salt-lake-city-2/450sx", "https://racerxonline.com/results/2021/salt-lake-city-1/450sx"] ## race result urls

finalResults = []
temp = []
index = 0

for i in urls:
    contents = readContents( urls[index] )
    temp = toTable (contents )

    finalResults = combineTable(temp, finalResults)

    index +=1

print (finalResults)














####### Notes ##########
##raceResults[1].append(2)
#print(raceResults[0]," " , raceResults[1])

## Goal:
## [["Name", [11,4,41,2]],
## [["Cooper Webb", 1],
##  ["Marvin Musquin", 2]]
##  ......

##t = resultsSoup.get_text()