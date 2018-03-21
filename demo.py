#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
import time
from conf import conf


class SeleniumDemo(object):
	"""docstring for SeleniumDemo"""
	def __init__(self):
		super(SeleniumDemo, self).__init__()
		# 驱动文件位置 D:\Python27\geckodriver.exe
		self.br = webdriver.Firefox()

	def elXpath(self, xpath):
		return self.br.find_element_by_xpath(xpath)

	def action(self):
		self.br.get(conf["product"]["getUrl"])

		uname = self.elXpath(conf["product"]["elements"]["uname"])
		upass = self.elXpath(conf["product"]["elements"]["upass"])
		loginBtn = self.elXpath(conf["product"]["elements"]["loginBtn"])

		# login
		uname.send_keys(conf["product"]["sendKeys"]["uname"])
		upass.send_keys(conf["product"]["sendKeys"]["upass"])
		loginBtn.click()
		print(self.br.title.encode('utf8'))
		time.sleep(1)

		# selectData
		selectData = self.elXpath(conf["product"]["elements"]["selectData"])
		selectData.click()
		selectYesterday = self.elXpath(conf["product"]["elements"]["selectYesterday"])
		selectYesterday.click()

		# checkCretText
		cretText = self.elXpath("/html/body/div/div/div/div/div[1]/div/span").text
		print(cretText.encode('utf8'))
		self.br.get_screenshot_as_file("xxx.png")

		time.sleep(1)
		self.br.close()

if __name__ == '__main__':
	sd = SeleniumDemo()
	sd.action()
