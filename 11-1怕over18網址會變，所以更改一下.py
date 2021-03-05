import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent
}

landingPageUrl ='https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
over18Url ='https://www.ptt.cc/'
pttUrl = 'https://www.ptt.cc/bbs/Gossiping/index.html'

ss = requests.session()

resLandindPage =ss.get(landingPageUrl,headers=headers)
soupLandindPage = BeautifulSoup(resLandindPage.text,'html.parser')

data =dict()
#for hidden value
hiddenKey =soupLandindPage.select('input')[0]['name']
hiddenValue =soupLandindPage.select('input')[0]['value']
data[hiddenValue] =hiddenValue

#for button
buttonKey = soupLandindPage.select('button')[0]['name']
buttonValue = soupLandindPage.select('button')[0]['value']
data[buttonKey] =buttonValue

print(data)
print(ss.cookies)

#get cookies 但怕over18網址會變，所以更改一下
over18Url += soupLandindPage.select('form')[0]['action']
ss.post(over18Url,data=data)
print(ss.cookies)

res = ss.get(pttUrl,headers=headers)
print(res.text)