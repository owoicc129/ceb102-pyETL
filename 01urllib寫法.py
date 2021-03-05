from urllib import request
# import ssl  (mac電腦會吃不到ssl憑證 所以要多一步驟)
# ssl._create_default_https_context = ssl._create_unverified_context()


userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers ={
    'User-Agent':userAgent
}

url ="https://www.ptt.cc/bbs/joke/index.html"


req = request.Request(url=url,headers=headers)
res = request.urlopen(req)
html=res.read().decode('utf-8')
print(html)