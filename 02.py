from urllib import request
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent
}
url ="https://www.ptt.cc/bbs/joke/index.html"

req = request.Request(url=url,headers=headers)
res = request.urlopen(req)
html=res.read().decode('utf-8')
# print(html)


soup = BeautifulSoup(html)
# print(soup)

logo = soup.findAll('a',{'id':'logo'})
print(logo) #list型式
# print(logo[0])
# print(type(logo[0])) #發現也是beautoful soup型式
# print(logo[0].text)
# print(logo[0]['href'])

# bbsContent = soup.findAll('div', class_= 'bbs-content')
# #會回傳在最外層html裡被div標籤 所包住的東西
# print(bbsContent[0])
# print('=============')
# #此時在進行一次用div，會回傳在最外層div裡被div包住的部分，會發現沒東西
# print(bbsContent[0].findAll('div'))
# print('=============')
# #如果此時要找div裡面的標籤a
# print(bbsContent[0].findAll('a'))