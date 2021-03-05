#如果有遇到json.decoder.JSONDecodeError問題，去看老師這篇github的code
#https://github.com/uuboyscy/ceb102-course/blob/master/ceb102-pyetl/15-techOrange.py
# 要爬這'https://buzzorange.com/techorange/'
import requests
import json
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
#這網址直接打開是空白的 但他是ajax所以嫌疑很大
url ='https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

#手動輸入 有問題再說，但我發現他的nonce是隨機 所以每次都要改
data ={
    'action': 'fm_ajax_load_more',
    'nonce': '4ba99f27ba',
    'page': 1
}


for p in range(3):
    print('[Page:{}]'.format(data['page']))

    res =requests.post(url,headers=headers,data=data)
    jsonData =json.loads(res.text)
    htmlStr =jsonData['data']
    soup =BeautifulSoup(htmlStr,'html.parser')

    for titleSoup in soup.select('h4[class="entry-title"]'):
        # print(titleSoup.a) #的a標籤
        title = titleSoup.a.text
        articleUrl = titleSoup.a ['href']
        print(title)
        print(articleUrl)
        print('=============')

    data['page'] += 1


