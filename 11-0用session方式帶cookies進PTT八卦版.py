import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent
}

#第一個要進去訪問的網址，是搜尋PTT八卦板時，可以點進去的那個
landingPageUrl ='https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
#第二個要進去的網址是F12 element裡，from action 寫的 會被帶到哪的網址
over18Url ='https://www.ptt.cc/ask/over18'
#第三個是 進去之後 八卦版的網址
pttUrl = 'https://www.ptt.cc/bbs/Gossiping/index.html'

ss = requests.session()

resLandindPage =ss.get(landingPageUrl,headers=headers)
soupLandindPage = BeautifulSoup(resLandindPage.text,'html.parser')


#把需要的資料 放在data字典裡
data =dict()
#需要那個在 element裡 input type=hidden 的標籤
hiddenKey =soupLandindPage.select('input')[0]['name']
hiddenValue =soupLandindPage.select('input')[0]['value']
data[hiddenKey] =hiddenValue
#需要那個 確認18按鈕按下去 會送出的資料
buttonKey = soupLandindPage.select('button')[0]['name']
buttonValue = soupLandindPage.select('button')[0]['value']
data[buttonKey] =buttonValue

print(data)
# print(ss.cookies) #看一下身上現在有什麼cookies，但會發現沒有那個over18的cookies

#get cookies 這是session自動把沿途經過的cookies設定到session裡
ss.post(over18Url,data=data)
# print(ss.cookies) #再看一次 會看到身上已經有over18的cookies，已經可以進入八掛版了



res = ss.get(pttUrl,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
# print(soup)