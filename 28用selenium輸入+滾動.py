from selenium.webdriver import Chrome
import time

driver = Chrome('./chromedriver')
url ='https://www.dcard.tw/f'
driver.get(url)
#找到框框標籤 輸入攝影
driver.find_element_by_tag_name('input').send_keys('攝影')

#點選查詢的按鈕，方法一:直接用xpath路徑的方式訂位(要先在框框內打字"攝影")(找到按鈕標籤位置-按右鍵copy-選fullXpath)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/form/button[2]').click()
#點選查詢的按鈕，方法二:用class訂位
# driver.find_element_by_class_name('dj0ioy-3.jCPeIq').click()
time.sleep(3)
#讓他滾動(element旁的console最底下框打:document.documentElement.scrollTop=5000)
driver.execute_script('vars =document.documentElement.scrollTop=15000')
time.sleep(5)
driver.execute_script('var s = document.documentElement.scrollTop=1')
# 取得目前的 html 字串
html = driver.execute_script("return document.getElementsByTagName('html')[0].outerHTML")
print(html)



