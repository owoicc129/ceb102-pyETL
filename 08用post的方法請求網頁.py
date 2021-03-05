import  requests

#這是一個用來給開發人員測試的post網站
url ="http://httpbin.org/post"
headers ={
    'User-Agent':'213215132sdadasd' #隨便打
}
data ={
    'key1':'value1',    #假想一些Data，主要是看那個網站要打幾的格子
    'key2':'value2'
}
res =requests.post(url,data=data,headers=headers)
print(res.text)


#用另一個post網頁測試~不過這網站突然進不去了
# url ='http://e2c30d442303.ngrok.io/hello_post'
# data ={
#     'username':'Allen'
# }
# res =requests.post(url,data=data)
# print(res.text)
