import urllib.request
from bs4 import BeautifulSoup

URL = 'http://cafe118.daum.net/_c21_/bbs_list?grpid=aVeZ&fldid=8lcX'
FILE_NAME = 'result.txt'

def crawling(URL) :
    source_code = urllib.request.urlopen(URL)
    sour = BeautifulSoup(source_code, 'lxml', from_encoding='utf-8')

    text = ''
    # for item in sour.find_all('div', id='articleBodyContents') :
    #     text += str(item.find_all(text=True))
    return str(sour)

myfile = open(FILE_NAME, 'w')
text = crawling(URL)
myfile.write(text)
myfile.close()
