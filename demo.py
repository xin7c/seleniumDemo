#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
import time
browser = webdriver.Firefox()
# 驱动文件位置 D:\Python27\geckodriver.exe
browser.get('http://devtest.adinsights.cn:9000/admin/#/')

uname = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/input[1]")
upass = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/input[2]")
loginBtn = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div[3]")

# login
uname.send_keys("zhangliang@reyun.com")
upass.send_keys("reyun123")
loginBtn.click()
print browser.title
time.sleep(1)
# 点击第一个审核

auditLinkOne = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/table/tr[2]/td[6]')
print auditLinkOne
auditLinkOne.click()

time.sleep(5)
browser.close()