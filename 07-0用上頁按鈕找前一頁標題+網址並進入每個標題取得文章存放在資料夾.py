import  requests
import  os
import time
import random
from bs4 import BeautifulSoup

#建立放文章內容的資料夾，如果不存在 就創
folderName ='pttMovie'
if not os.path.exists(folderName):
    os.mkdir(folderName)

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent
}
url ="https://www.ptt.cc/bbs/movie/index.html"


for i in range(5):
    res = requests.get(url,headers=headers)
    soup =BeautifulSoup(res.text,'html.parser')
    title = soup.select('div.title')
    print(title)

    for titleSoup in title:
        # titles = titleSoup.select('a')
        titles = titleSoup.select_one('a').text
        print(titles)
        url2 = "https://www.ptt.cc" + titleSoup.select_one('a')['href']
        print(url2)
        resArticle = requests.get(url2,headers=headers)
        soupArticle =BeautifulSoup(resArticle.text,'html.parser')
        articleContent = soupArticle.select('div[id="main-content"]')[0]

        #寫法一
        for i in articleContent.select('span'):
            i.extract()  #将当前tag移除文档树,并作为方法结果返回
        for i in articleContent.select('div'):
            i.extract()
        article = articleContent.text
        # #寫法二
        # for tag in ['span','div']:
        #     for i in articleContent.select(tag):
        #         i.extract()
        # article = articleContent.text




        try:
            #建立資料夾 路徑為 資料夾/標題名稱.txt
            with open(folderName + '/' + titles +'.txt', 'w', encoding='utf-8') as f:
                f.write(article)
        except FileNotFoundError:
            with open(folderName+'/'+titles.replace('/','-')+'.txt', 'w', encoding='utf-8') as f:
                f.write(article)
        except OSError:
            pass

        time.sleep(random.randint(1,10)/100) #产生 1 到 10 的一个整数型随机数 再除100




    lastPageButton = soup.select('a[class="btn wide"]')
    # print(lastPageButton)
    lastPageUrl = 'https://www.ptt.cc' + lastPageButton[1]['href']
    print(lastPageUrl)

    url = lastPageUrl