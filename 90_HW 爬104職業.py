import requests
import json
import pprint
from bs4 import BeautifulSoup
import pandas as pd


userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent
}

ss = requests.session()
a=10 #因為第一頁的前10個會是至頂廣告
data = [] #把取得的資訊都放入list

for i in range(1,4): #自訂爬幾頁
    url = f'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90&order=12&asc=0&page={i}&mode=s'
    res = ss.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    # print(soup)


    links = soup.select('a.js-job-link')[a:]  #取出這一頁所有職位的網址
    for link in links:
        link = link["href"].split("?")[0].split("/")[-1]
        # print(link)

        headers_content = {
            'User-Agent': userAgent,
            'Referer': f'https://www.104.com.tw/job/{link}?jobsource=jolist_b_relevance'
        }
        url_content = f'https://www.104.com.tw/job/ajax/content/{link}'

        res =ss.get(url=url_content,headers=headers_content)  #進入文章
        # print(res.text)
        jsonData = json.loads(res.text)
        # pprint.pprint(jsonData)

        custName = jsonData['data']['header']['custName']
        jobName = jsonData['data']['header']['jobName']
        jobDescription = jsonData['data']['jobDetail']['jobDescription']
        otherCondition = jsonData['data']['condition']['other']
        # print(custName)
        # print(jobName)
        # print(jobDescription)
        # print(otherCondition)
        # print("==========")

        data.append([custName,jobName,jobDescription,otherCondition])
        a=0
#     print(url)
# pprint.pprint(data)

columns= ['公司名稱','職位名稱','工作內容','加分條件']
df = pd.DataFrame(data=data, columns=columns)
print(df)
df.to_csv(r'./104_jobList.csv',index=False,encoding='utf-8-sig')