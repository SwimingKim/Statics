import urllib.request
from bs4 import BeautifulSoup
from operator import eq

URL = 'http://m.cafe.daum.net/ok1221/8lcX?boardType='
FILE_NAME = 'daum.txt'

def crawling(URL) :
    source_code = urllib.request.urlopen(URL)
    sour = BeautifulSoup(source_code, 'lxml', from_encoding='utf-8')

    text = ''
    for item in sour.find_all('li', class_='cmt_none') :
        for txt in item.find_all('span', class_='txt_detail') :
            txt = str(txt.find_all(text=True))
        for day in item.find_all('span', class_='num_info') :
            day = day.find(text=True)
            break
        text += 'txt='+txt+'day='+day+"\n"
    return text

    self.log(text)

myfile = open(FILE_NAME, 'w')
text = crawling(URL)
myfile.write(text)
myfile.close()
