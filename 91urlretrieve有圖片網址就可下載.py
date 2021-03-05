#下載圖片寫法 用到urllib裡的request裡的urlretrieve(圖片網址+存放位置)

import os
from urllib import request


imgFolder = '爬蟲實戰/'
if not os.path.exists(imgFolder):
    os.mkdir(imgFolder)

for i in range(227):
    url = f'https://image.slidesharecdn.com/python-170809083644/95/python-{i+1}-1024.jpg?cb=1502702196'
    imgPath = imgFolder + f'Python爬蟲實戰第{i+1}頁' + '.jpg'
    request.urlretrieve(url, imgPath)