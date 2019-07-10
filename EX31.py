"""
 File Name: EX31.py
 Version  : 1.0
 Author   : Gary
 Date     : 2018/12/6 16:17
 Software : PyCharm
 
"""
from selenium import webdriver

driver = webdriver.Firefox()

url = 'https://www.baidu.com'

driver.get(url)

driver.close()

#driver.quit()