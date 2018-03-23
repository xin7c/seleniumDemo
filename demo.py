#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
import time
from conf import conf
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class SeleniumDemo(object):
    """selenium自动化测试demo"""

    def __init__(self):
        super(SeleniumDemo, self).__init__()
        # 驱动文件位置 D:\Python27\geckodriver.exe
        self.br = webdriver.Firefox()

    def elXpath(self, xpath):
        return self.br.find_element_by_xpath(xpath)

    def saveScreenshot(self):
        picName = conf["path"]["screenShot"] + time.strftime("%m%d%H%M", time.localtime()) + ".png"
        print picName
        self.br.get_screenshot_as_file(picName)

    def action(self):
        self.br.get(conf["product"]["getUrl"])

        uname = self.elXpath(conf["product"]["elements"]["uname"])
        upass = self.elXpath(conf["product"]["elements"]["upass"])
        loginBtn = self.elXpath(conf["product"]["elements"]["loginBtn"])

        # login
        uname.send_keys(conf["product"]["sendKeys"]["uname"])
        upass.send_keys(conf["product"]["sendKeys"]["upass"])
        loginBtn.click()
        print(self.br.title)
        time.sleep(1)

        # selectData
        selectData = self.elXpath(conf["product"]["elements"]["selectDate"])
        selectData.click()
        selectYesterday = self.elXpath(conf["product"]["elements"]["selectYesterday"])
        selectYesterday.click()

        # checkCretText
        cretText = self.elXpath(conf["product"]["elements"]["cretText"]).text
        print(cretText)

        # checkProductList
        productTableGame = self.br.find_element_by_xpath(conf["product"]["elements"]["productTableGame"])
        productTableGameTrList = productTableGame.find_elements_by_tag_name("tr")
        print(len(productTableGameTrList))

        for i, j in enumerate(productTableGameTrList):
            # 定位game表格的[投放计划]数值文本
            trXpathGame = conf["product"]["elements"]["trXpathGame"] % (str(i + 1))
            if i <= 2:
                print(i, self.elXpath(trXpathGame).text)
                print("-" * 10)
        self.saveScreenshot()
        time.sleep(1)
        self.br.close()


if __name__ == '__main__':
    sd = SeleniumDemo()
    sd.action()
