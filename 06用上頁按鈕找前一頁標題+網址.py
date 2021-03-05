import  requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent
}
url ="https://www.ptt.cc/bbs/movie/index.html"


for i in range(5):
    res = requests.get(url,headers=headers)
    soup =BeautifulSoup(res.text,'html.parser')
    titles = soup.select('div.title')
    # print(titles)

    for titleSoup in titles:
        try:
            # title = titleSoup.select('a')
            title = titleSoup.select_one('a').text
            print(title)
            url2 = "https://www.ptt.cc" + titleSoup.select_one('a')['href']
            print(url2)
        except AttributeError as e:
            print('===========')
            print(titleSoup.select_one)
            print(e.args)
            print('===========')


    lastPageButton = soup.select('a[class="btn wide"]')
    # print(lastPageButton) # btn wide有3個符合會回傳3個，這3個位置固定
    lastPageUrl = 'https://www.ptt.cc' + lastPageButton[1]['href']
    # print(lastPageUrl)

    url = lastPageUrl