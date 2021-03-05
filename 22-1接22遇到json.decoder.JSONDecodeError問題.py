#22 遇到json.decoder.JSONDecodeError問題

import requests
import json
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}

url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

data = {
    'action': 'fm_ajax_load_more',
    'nonce': '64b097bf9a',
    'page': 1
}

for p in range(0, 3):
    print('[Page: {}]'.format(data['page']))
    isRequestSuccess = False
    while isRequestSuccess == False:
        try:
            res = requests.post(url, headers=headers, data=data)
            jsonData = json.loads(res.text)
        except json.decoder.JSONDecodeError:
            time.sleep(3)
        else:
            isRequestSuccess = True
    # jsonData = res.json()
    htmlStr = jsonData['data']
    soup = BeautifulSoup(htmlStr, 'html.parser')

    for titleSoup in soup.select('h4[class="entry-title"]'):
        title = titleSoup.a.text
        articleUrl = titleSoup.a['href']
        print(title)
        print(articleUrl)
        print('======')

    data['page'] += 1
    time.sleep(3)