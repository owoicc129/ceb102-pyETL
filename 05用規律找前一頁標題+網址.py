import  requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent
}
url ="https://www.ptt.cc/bbs/movie/index{}.html"
page =9498

#假設抓5頁
for i in range(5):
    # print('[page:{}]'.format(page)) #告訴你現在你在哪頁
    print(f'[page:{page}]')

    res = requests.get(url.format(page),headers=headers)
    soup =BeautifulSoup(res.text,'html.parser')
    titles = soup.select('div.title')
    # print(titles)

    for titleSoup in titles:
        title = titleSoup.select('a')[0].text
        # title = titleSoup.select_one('a').text
        print(title)
        url2 = "https://www.ptt.cc"+titleSoup.select_one('a')['href']
        print(url2)


    page -=1