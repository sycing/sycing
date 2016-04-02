#coding:utf-8
import os
from selenium import webdriver
from time import sleep
'''
chromedriver='C:\Drivers\chromedriver_win32\chromedriver.exe'
os.environ['webbdriver,chrime.driver']=chromedriver
driver=webdriver.Chrome(chromedriver)
'''
driver=webdriver.Chrome()
#driver=webdriver.Firefox()
#driver=webdriver.Ie()
driver.get("http://www.baidu.com")
print( '浏览器最大化')
#driver.maximize_window()
sleep(3)

driver.find_element_by_id('kw').send_keys(u'web自动化测试')
driver.find_element_by_id('su').click()
sleep(10)
print 'done'
driver.quit()
