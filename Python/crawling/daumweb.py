import urllib
# import urllib2
from bs4 import BeautifulSoup
from operator import eq

URL = 'http://cafe.daum.net/ok1221/8lcX?prev_page=1&firstbbsdepth=1hac7&lastbbsdepth=1habo&page=1'
FILE_NAME = 'daumweb.html'

def crawling(URL) :
    source_code = urllib.request.urlopen(URL).read()
    sour = BeautifulSoup(source_code, 'html.parser', from_encoding='utf-8')

    # table = sour.find("table", { "class" : "lineItemsTable" })
    # for row in table.find_all("tr") :
    #     cells = row.find_all("td")
    #     print(cells)


    text = ''
    for row in sour.find_all('tr') :
        print(row)
        text += row.find_all(text=True)
    return str(sour)


myfile = open(FILE_NAME, 'w')
text = crawling(URL)
myfile.write(text)
myfile.close()
