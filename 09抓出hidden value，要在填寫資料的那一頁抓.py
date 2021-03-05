import  requests
from bs4 import BeautifulSoup

# headers 是要字典形式
headersStr ='''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 441
Content-Type: application/x-www-form-urlencoded
Cookie: _ga=GA1.1.1805164871.1611974373; JSESSIONID=0000dAwZSr0FunGEtsRidIWNZgw:148b36dur; NSC_xfc_qfstjtufodf=ffffffff09081f7445525d5f4f58455e445a4a423660; cookiesession1=1EF25D71L15OGJW3M5JQAUJZGXGM1D3B; _ga_Y7WTCDJF3D=GS1.1.1612075222.3.1.1612075439.0
Host: web.pcc.gov.tw
Origin: https://web.pcc.gov.tw
Referer: https://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'''

headers = dict()
for row in headersStr.split('\n'):
    headers[row.split(': ')[0]] =row.split(': ')[1]
print(headers)


# data 也是要字典形式
dataStr ='''method: search
searchMethod: true
searchTarget: ATM
orgName: 1111
orgId: 
hid_1: 1
tenderName: 111
tenderId: 
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 110/01/28
awardAnnounceEndDate: 110/01/28
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: 11
hid_2: 1
gottenVendorName: 11
gottenVendorId: 
hid_3: 1
submitVendorName: 1
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢'''

data ={row.split(': ')[0]: row.split(': ')[1] for row in dataStr.split('\n') if row != ' '}  # if row != ' ' 是額外 可加可不加
# print(data)

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'

# 老師發現用上面的 headers 進不去網頁，所以重新隨便用一個headers就可以進了
headers ={
    'User-Agent':userAgent
}

url ='https://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM'
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
hiddenInput = soup.select('input[type="hidden"]')  #有隱藏的都會是input[type="hidden"]
# print(hiddenInput)


hiddenData = dict()
for i in hiddenInput:
    try:
        hiddenData[i['name']] = i['value'] # i的name,i的value
    except:
        pass # 因為不是每個input 都有value
# print(hiddenData)