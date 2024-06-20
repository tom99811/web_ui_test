#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import unittest
import sys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils.logger import Logger
from data.config import Config

logger = Logger(logger="BrowserDriver").getlog()


class BrowserDriver(object):

    def __init__(self):
        self.c = Config()
        path = './drivers/'  # 这是获取相对路径的方法
        if sys.platform.startswith('win'):
            self.chrome_driver_path = path + 'chromedriver.exe'
        else:
            self.chrome_driver_path = path + 'chromedriver'

    def openbrowser(self):
        browser = self.c.get("browserType", "browserName")
        logger.info("选择的浏览器为: %s 浏览器" % browser)
        url = self.c.get('ptahUrl', "URL")
        logger.info("读取到的URL为: %s" % url)
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("启动火狐浏览器")
        else:
            chrome_options = Options()
            me = {"deviceName": "iPhone 6"}
            # chrome_options.add_experimental_option("mobileEmulation", me)
            chrome_options.add_experimental_option('mobileEmulation', me)
            chrome_options.binary_location = "/Users/ellan/pythonProject/SixTSportUI/drivers/chromedriver"
            chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
            # chrome_options.add_argument('--start-maximized')  # 指定浏览器分辨率
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
            # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('lang=zh_CN.UTF-8')
            driver = webdriver.Chrome(options=chrome_options)
            # driver = webdriver.Chrome(self.c.driver_ptah()) #用于Windows系统加载驱动使用
            # driver = webdriver.Chrome() #用于linux系统加载驱动使用
            logger.info("启动谷歌浏览器")
            driver.implicitly_wait(5)
            logger.info("设置5秒隐式等待时间")

            driver.get(url)
            logger.info("打开URL: %s" % url)

            time.sleep(5)

            # 隐藏首页弹窗广告
            logger.info("隐藏首页弹窗广告")
            js = "document.querySelectorAll('.rv-overlay.announcement.rv-fade-enter-done').forEach(element => {element.style.display = 'none';});"
            driver.execute_script(js)

        return driver

    @classmethod
    def quit_browser(self, driver):
        logger.info("关闭浏览器")
        driver.quit()


class Model(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # username = c.get_case_data('login').get('username')
        # password = c.get_case_data('login').get('password')
        driver = BrowserDriver()
        cls.driver = driver.openbrowser()
        return cls.driver

    def setUp(self):
        # driver = BrowserDriver()
        # driver.openbrowser()
        pass

    def teardown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    driver = BrowserDriver()
    driver.openbrowser()

