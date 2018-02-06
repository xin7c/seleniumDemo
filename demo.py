#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
import time
class SeleniumDemo(object):
	"""docstring for SeleniumDemo"""
	def __init__(self):
		super(SeleniumDemo, self).__init__()
		# 驱动文件位置 D:\Python27\geckodriver.exe
		self.browser = webdriver.Firefox()

	def action(self):
		self.browser.get('http://devtest.adinsights.cn:9000/admin/#/')
		uname = self.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/input[1]")
		upass = self.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/input[2]")
		loginBtn = self.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div[3]")

		# login
		uname.send_keys("zhangliang@reyun.com")
		upass.send_keys("reyun123")
		loginBtn.click()
		print self.browser.title.encode('utf8')
		time.sleep(1)
		# 点击第一个审核
		auditLinkOne = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/table/tr[2]/td[6]')
		print auditLinkOne
		auditLinkOne.click()

		time.sleep(5)
		self.browser.close()

if __name__ == '__main__':
	sd = SeleniumDemo()
	sd.action()