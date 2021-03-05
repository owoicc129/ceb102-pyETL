from urllib import request
import  requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent
}
url ="https://www.ptt.cc/bbs/joke/index.html"

# urllib寫法
# req = request.Request(url=url,headers=headers)
# res = request.urlopen(req)
# # 不用寫res.read().decode('utf-8'),因為有html.parser
# soup = BeautifulSoup(res,'html.parser')
# print(soup)

#requsets 寫法
res =requests.get(url,headers=headers)
print(res.text) #會回傳<Response [200]>,所以需要.text
soup = BeautifulSoup(res.text,'html.parser')
print(soup)