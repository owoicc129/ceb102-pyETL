from urllib import request

url ="http://e2c30d442303.ngrok.io/hello_get"

res = request.urlopen(url=url)

print(res.read().decode('utf-8'))