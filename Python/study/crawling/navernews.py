from bs4 import BeautifulSoup
import urllib.request

URL = 'http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=421&aid=0002627761&date=20170323&type=1&rankingSeq=2&rankingSectionId=100'
RESULT = 'sewol.txt'

def crawling(URL) :
    from_url = urllib.request.urlopen(URL)
    soup = BeautifulSoup(from_url, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='articleBodyContents') :
        text += str(item.find_all(text=True))
    return text

myfile = open(RESULT, 'w')
text = crawling(URL=URL)
myfile.write(text)
myfile.close()
