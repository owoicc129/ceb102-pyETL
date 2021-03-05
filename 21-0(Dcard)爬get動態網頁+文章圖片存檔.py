import requests
import json
import pprint
from urllib import request
import os

dcardFolder = 'dcard/'
if not os.path.exists(dcardFolder):
    os.mkdir(dcardFolder)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
#這網址最多就30篇文章
url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=235214594'

'''
res = requests.get(url, headers=headers)
print(res.text)  #此處老師可印出json 
jsonData = json.loads(res.text) # list
for i in jsonData:
    print(i)

目前因為無法從網頁爬下JSON，改用手動創檔案 並複製JSON入檔
(json.decoder.JSONDecodeError 是因為被檔 所以無法取得JSON格式)
'''


#改用手動創檔案 (開檔並把json字串load成json)
with open ('jsondata.json','r',encoding='utf-8') as f:
    jsonData = json.loads(f.read()) #list

pprint.pprint(jsonData[0])
# print(jsonData[0].keys()) #資料太大可先看key直有哪些

# 發現文章的網址跟id有關
# 圖片跟mediaMeta有關
# 標題跟title有關


#先取標題跟網址
for articleObj in jsonData:
    title = articleObj['title']
    articleUrl = 'https://www.dcard.tw/f/photography/p' + str(articleObj['id']) #轉成字串
    print(title)
    print(articleUrl)

    #發現圖片是list型式，每張圖都被包在一個字典裡
    for n,imgInfo in enumerate(articleObj['mediaMeta']):
        tmpImgUrl =imgInfo['url']
        print('\t', tmpImgUrl)  # 會加tab縮排

        #下載圖片寫法1 用到urllib裡的request裡的urlretrieve(圖片網址+存放位置)
        # request.urlretrieve(tmpImgUrl,dcardFolder + tmpImgUrl.split('/')[-1])
        # 或給每張圖檔名
        imgPath = dcardFolder + title + ' ' + str(n) + '.' + tmpImgUrl.split('.')[-1]
        # request.urlretrieve(tmpImgUrl,imgPath)

        #下載圖片寫法2 把圖片變成二進位文字儲存 .content
        resImg =requests.get(tmpImgUrl,headers=headers)
        imgContent = resImg.content
        # print(imgContent) #會看到一堆二進位文字

        with open (imgPath,'wb') as f:  #寫入二進制
            f.write(imgContent)
    print('=========')



