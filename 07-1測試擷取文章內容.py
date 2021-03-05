import  requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent
}
url2 ="https://www.ptt.cc/bbs/movie/M.1612016560.A.90E.html"

resArticle = requests.get(url2,headers=headers)
soupArticle =BeautifulSoup(resArticle.text,'html.parser')
articleContent = soupArticle.select('div[id="main-content"]')[0]
# print(articleContent)
# print(articleContent.text)
# print(articleContent.text.split('※ 發信站')[0])

for i in articleContent.select('span'):
    print(i)
#     i.extract() #将当前tag移除文档树,并作为方法结果返回
# for i in articleContent.select('div'):
#     i.extract()
# print(articleContent)
# print(articleContent.text)