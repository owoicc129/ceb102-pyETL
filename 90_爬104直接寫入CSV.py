# 使用套件
import requests
from bs4 import BeautifulSoup as bs
import csv
import time

# 由於頁面我們要抓很多頁因此拆開兩個網址相加
url_A = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=python&order=15&asc=0&page='
url_B = '&mode=s&jobsource=2018indexpoc'

# 設定一個list
datas = []
for page in range(1, 6):
    url = url_A + str(page) + url_B

    htmlFile = requests.get(url)
    soup = bs(htmlFile.text, 'html.parser')
    # 104的頁面區塊是article中的jsjob item
    jobs = soup.find_all('article', class_='js-job-item')  # 搜尋所有職缺

    # 我們分別
    for i in jobs:
        name = i.find('a', class_="js-job-link").text  # 職缺內容
        company = i.get('data-cust-name')  # 公司名稱
        address = i.find('ul', class_='job-list-intro').find('li').text  # 地址
        salary = i.find('span', class_='b-tag--default').text  # 薪資
        url = 'http:' + i.find('a').get('href')  # 網址
        job_data = {'職缺內容': name, '公司名稱': company, '地址': address, '薪資': salary, '網址': url}
        datas.append(job_data)
    # 每抓完一頁休息3秒鐘 避免被擋住IP
    time.sleep(3)

fn = '104人力銀行職缺內容共5頁.csv'  # 取CSV檔名
columns = ['職缺內容', '公司名稱', '地址', '薪資', '網址']  # 第一欄的名稱
with open(fn, 'w', newline='', encoding='utf-8-sig') as csvFile:  # 定義CSV的寫入檔,並且每次寫入完會換下一行
    Hbank = csv.DictWriter(csvFile, fieldnames=columns)  # 定義寫入器
    Hbank.writeheader()
    for data in datas:
        Hbank.writerow(data)