import  requests
from bs4 import BeautifulSoup
import  os
import json
import pprint


folderName ='591house'
if not os.path.exists(folderName):
    os.mkdir(folderName)

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent,
    'X-CSRF-TOKEN': 'DF8SmTk7o0YkI2L7MLcTHRpsRZ1ahj36ObzDICpd',  #會變要改
    'Cookie':'__utmz=82835026.1609161821.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __auc=f444c3b6176a984cb3f3b6a22ff; is_new_index=1; is_new_index_redirect=1; T591_TOKEN=h76so7pnnir0totin8t1mdp1f2; tw591__privacy_agree=0; _ga=GA1.4.185933412.1609161821; user_index_role=1; _fbp=fb.2.1609330609792.1548719655; new_rent_list_kind_test=0; __utma=82835026.185933412.1609161821.1609161821.1613572761.2; last_search_type=1; urlJumpIpByTxt=%E5%8F%B0%E5%8C%97%E5%B8%82; urlJumpIp=1; index_keyword_search_analysis=%7B%22role%22%3A%221%22%2C%22type%22%3A%221%22%2C%22keyword%22%3A%22%22%2C%22selectKeyword%22%3A%22%22%2C%22menu%22%3A%22%22%2C%22hasHistory%22%3A0%2C%22hasPrompt%22%3A0%2C%22history%22%3A0%7D; _gid=GA1.3.1290798883.1613979027; _gid=GA1.4.1290798883.1613979027; user_browse_recent=a%3A5%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A8%3A%2210530262%22%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A8%3A%2210416992%22%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A8%3A%2210421510%22%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A8%3A%2210432569%22%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A8%3A%2210507469%22%3B%7D%7D; webp=1; PHPSESSID=6o4ujga44bggepnsfpn0julgs1; XSRF-TOKEN=eyJpdiI6IjVWMTJST3NVdG85RWhMTTVxb2NVWFE9PSIsInZhbHVlIjoiM2ZMaksrT0lnMGZwU1RTOEFLNVoxdmFrRW1lSUxQWVRKR1dZdjF0cE42VHFHeVZGNWxabjJDV0FWSHhYWFZFMFBzNlBxMlwvNDVIdUdadzFqNlhhYnd3PT0iLCJtYWMiOiIzNGVhMTc3Mzg2YTZmNWRhOTE5MWFjYmVjMjg5MzFiYjQyOWVjYTU1YmIyNjJkMWY1OWI5NmZlMzc5MjI1YjlmIn0%3D; 591_new_session=eyJpdiI6IkV1Wnk4XC91UlBDMlwvKzB3RkNXQlA2Zz09IiwidmFsdWUiOiJJYklVRWZKZXluSG5BblZ6aFR5SUZHZ2VkZyt0ZzNITXJmSm11UURsTzdlUXQxTzU0UmVySnhUaElRTnN6SWlUN3lZM0E5TE1qamt5QnRPbTY5K3h1dz09IiwibWFjIjoiODYzOGUwMTAzZDIyZGQwZjhiMjFlNDBkMmU1N2FhZGUzYTcxODgyMjE3ODg4ZjQ2M2MyM2U2NWI0MTgxZmQ1MyJ9; _ga=GA1.3.185933412.1609161821; _gat_UA-97423186-1=1; _ga_ZDKGFY9EDM=GS1.1.1614056891.14.1.1614057045.0'
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Connection': 'keep-alive',
    # 'Host': 'rent.591.com.tw',
    # 'Referer': 'https://rent.591.com.tw/?kind=0&region=1',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'X-Requested-With': 'XMLHttpRequest'
}

page = 1  #手動改你要的頁數 (每30筆是一頁)
#進入租屋網頁 https://rent.591.com.tw/?kind=0&region=1 開Network找到每頁資料都在rslist裡
for i in range(page):
    rsList_url= f'https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=1&firstRow={i*30}' #發現規律 第一頁0,第二頁30,第三頁60,第四頁90 以此推

    ss = requests.session()
    res =ss.get(rsList_url,headers=headers)
    # print(res.text)

    jsonData = json.loads(res.text)
    pprint.pprint(jsonData)
    # pprint.pprint(jsonData['data']['data'])
    #
    # for x,id in enumerate(jsonData['data']['data']):
    #     # print(x,id['id'])
    #     id = id['id']
    #
    #     article_url = f'https://rent.591.com.tw/rent-detail-{id}.html'
    #     res = ss.get(url=article_url,headers=headers)
    #     soup =BeautifulSoup(res.text,'html.parser')
    #     # print(soup)
    #     print(article_url)
    #     try:
    #         info = soup.select('div.houseIntro')[0].text
    #         title = soup.select('span.houseInfoTitle')[0].text
    #         price = soup.select('div.price.clearfix')[0].text
    #         lifebox = soup.select('div.lifeBox')[0].text
    #         # # pic =soup.select('textarea.datalazyload')[0]('img')[0]['src'].split('_')[0]
    #         pics = soup.select('textarea.datalazyload')[0]('img')
    #         print(title)
    #     except IndexError:
    #         pass
    #
    #     #抓圖片
    #     for i, pic in enumerate(pics):
    #         picUrl = pic['src'].split('_')[0] + '_765x517.water3.jpg'
    #         resImg = ss.get(picUrl, headers=headers)
    #         imgContent = resImg.content
    #         try:
    #             with open(folderName + '/' + title + f'{i + 1}.jpg', 'wb') as f:  # 寫入二進制
    #                 f.write(imgContent)
    #         except FileNotFoundError:
    #             title = title.replace('/', '')
    #             with open(folderName + '/' + title + f'{i + 1}.jpg', 'wb') as f:  # 寫入二進制
    #                 f.write(imgContent)
    #         except OSError:
    #             title = title.replace('*', '')
    #             with open(folderName + '/' + title + f'{i + 1}.jpg', 'wb') as f:  # 寫入二進制
    #                 f.write(imgContent)
    #
    #     #文字寫檔
    #     try:
    #         with open(folderName + '/' + title + '.txt', 'a', encoding='utf-8') as f:
    #             f.write(title)
    #             f.write('\n')
    #             f.write(price)
    #             f.write('\n')
    #             f.write(lifebox)
    #             f.write('\n')
    #             f.write(info)
    #     except FileNotFoundError:
    #         title = title.replace('/', '')
    #         print(title)
    #         with open(folderName + '/' + title + '.txt', 'a', encoding='utf-8') as f:
    #             f.write(title)
    #             f.write('\n')
    #             f.write(price)
    #             f.write('\n')
    #             f.write(lifebox)
    #             f.write('\n')
    #             f.write(info)
    #     except OSError:
    #         title = title.replace('*', '')
    #         with open(folderName + '/' + title + '.txt', 'a', encoding='utf-8') as f:
    #             f.write(title)
    #             f.write('\n')
    #             f.write(price)
    #             f.write('\n')
    #             f.write(lifebox)
    #             f.write('\n')
    #             f.write(info)
    #
