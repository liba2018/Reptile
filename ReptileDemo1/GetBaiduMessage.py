from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#chromedriverpath = 'D:/Python/Python37/chromedriver.exe'
#driver = webdriver.Chrome(chromedriverpath)
driver = webdriver.Chrome()

#打开目标网页
driver.get("http://baidu.com")

#获取网页标题
title = driver.title
#获取输入框输入搜索内容
word = driver.find_element_by_name('wd')
word.send_keys('马云')
#回车确认
word.send_keys(Keys.RETURN)

#暂停时间获取页面渲染（这个很重要，页面加载需要时间）
time.sleep(5)
#获取搜索的html
html = driver.page_source

print(title)
print('----------------------------------------------------------------------------------------------')
#打印内容
print(html)
#其他api请自行百度
#...

driver.close()
