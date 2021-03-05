# 591租屋網
import requests
from bs4 import BeautifulSoup
import json

# 連入首頁
url = 'https://rent.591.com.tw/'
ss = requests.session()
res = ss.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# 取得csrf-token
csrfToken = soup.findAll("meta", {"name": "csrf-token"})[0]['content']

# 取得Cookie
cookie = '591_new_session=' + dict(res.cookies).get('591_new_session')

# 建立headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'X-CSRF-TOKEN': csrfToken,
    'Cookie': cookie
}

# 查詢頁面網址
url = 'https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=1&firstRow=30'
res = requests.get(url, headers=headers)

# 取得搜尋結果
jsonData = json.loads(res.text)
print(jsonData)