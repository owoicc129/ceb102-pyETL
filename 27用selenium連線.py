from selenium.webdriver import Chrome

driver = Chrome('./chromedriver') #Driver路徑，不用打exe

#用Driver連線
driver.get('https://www.ptt.cc/bbs/index.html')

#定位class標籤'board-name'(會有很多個)，但因為八卦版在第一個 就直接訂位到
driver.find_element_by_class_name('board-name').click()
#再點選滿18
driver.find_element_by_class_name('btn-big').click()
#印出cookies
cookie = driver.get_cookies()
for i in cookie:
    print(i)



#==========================================
#elements複數定位，可選你要第幾個'board-name'
# driver.find_elements_by_class_name('board-name')[2].click()