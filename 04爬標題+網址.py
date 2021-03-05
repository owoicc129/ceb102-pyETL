import  requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent
}
url ="https://www.ptt.cc/bbs/movie/index.html"

res = requests.get(url,headers=headers)

soup =BeautifulSoup(res.text,'html.parser')
# print(soup.prettify()) #美觀

title = soup.select('div.title')
# print(title)
# print(title[0]) #看看第0

for titleSoup in title:
    # print(titleSoup)
    # titles = titleSoup.select('a') #每個都是list
    titles = titleSoup.select('a')[0].text
    # titles = titleSoup.select_one('a').text
    print(titles)
    url = titleSoup.select('a')[0]['href']
    # url = titleSoup.select_one('a')['href']
    print('https://www.ptt.cc' + url)