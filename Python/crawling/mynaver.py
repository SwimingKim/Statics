import os
import sys
import urllib.request
client_id = "9SIyg9SqyQeza4hpRq7c"
client_secret = "T4y8PK6qm0"
encText = urllib.parse.quote("여대생")

# https://openapi.naver.com/v1/search/cafearticle.xml

url = "https://openapi.naver.com/v1/search/cafearticle?query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)