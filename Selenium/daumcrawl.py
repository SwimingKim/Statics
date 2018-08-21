# -*- codion: cp949 -*-

import urllib
import urllib.request
import time
import datetime
import random
from bs4 import BeautifulSoup
from operator import eq
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

s = datetime.datetime.now()
# driver = webdriver.Chrome(executable_path='/Users/suyoung/Documents/Dev/chromedriver')
driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
driver.get("http://m.cafe.daum.net/ok1221/8lcX?prev_page=2&firstbbsdepth=1ic8e&lastbbsdepth=1ic8J&page=1")

text = ''
exp_num = []
num_data = []
count = 0
FILE_NAME = 'result.txt'

# div와 같이 #으로 이어진 경우 중괄호 :를 써야함, ex. article#id=mArticle 인 경우 ("article", {"id":"mArticle"})
# for dum in sour.find_all("article", {"id":"mArticle"}) :

# a와 같이 .으로 이어진 경우 "해당 단어_"로 써도 됨 ex. li.class=  notice 인 경우 ("li", class_=" notice")
#     for item2 in sour.find_all("li", class_=" notice") :

#("li", class_=" ")을 사용하면 " notice"도 긁어짐, 아래와 같이 for문을 동시에 돌리려면 zip을 사용하면 됨
    #for item2, item3 in zip(sour.find_all("li", class_=" "), sour.find_all("li", class_=" notice")) :
        # if item2 == item3 :
        #     continue

def crawling() :
    global text, count, exp_num, num_data
    for i in range(1, 10, 1) :
        print("first i ", i)
        URL = driver.current_url

        source_code = urllib.request.urlopen(URL)
        sour = BeautifulSoup(source_code, 'lxml', from_encoding='utf-8')
        exp = ['------＜17학번 새내기 달글 6＞------- ','📢📢익담 자체공지 모르겠는 도토들은 모이세요📢📢','익담 공지  (고등학생 출입금지 / 남성출입금지)']

        print(URL)
        if count == 0 :
            num_count = 0
            for num in sour.find_all("span", class_="num_info") :
                if num_count >= 5 :
                    break
                dum_num = num.get_text()
                exp_num.append(dum_num)
                num_count += 1
                print(dum_num)

        num_count = 0
        for num_item in sour.find_all("span", class_="num_info") :
            temp2 = num_item.get_text()
            if temp2 in exp_num :
                continue
            else :
                if num_count%2 == 0 :
                    num_count += 1
                    continue
                else :
                    num_count += 1
                    num_data.append(temp2)
        for text_item, num_item2 in zip(sour.find_all("span", class_="text_detail"), num_data) :
            if eq(temp, exp[0]) or eq(temp, exp[1]) or eq(temp, exp[2]) :
                continue
            text += temp + '\t' + num_item2 + '\n'

        if i%5==0 :
            print("i", i)
            print("i+1", i+1)
            link2 = driver.find_element_by_link_text("다음페이지")
            link2.click()
            i += 2
            time.sleep(random.uniform(2, 3))

        else :
            link = driver.find_element_by_link_text(str(i+1))
            print("i", i)
            print("i+1", i+1)
            link.click()
            time.sleep(random.uniform(2, 3))
        count += 1

    return text

myfile = open(FILE_NAME, 'w')
text = crawling()
myfile.write(text)
myfile.close()
