#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

from selenium.webdriver.common.by import By
from test.common.Seleniums import BasePage
import sys

sys.path.append('../')


class SixTSport(BasePage):
    """在这里写定位器，通过元素属性定位元素对象,元素库"""
    # 登录页面
    idx_login_btn = (By.XPATH, '//*[@id="homepage"]/div[2]/div/div[1]/div[2]/a[2]')   # 首页登录按钮
    user_input_box = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/input')   # 登录页面user输入框
    psd_input_box = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/input')    # 登录页面密码输入框
    login_btn = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[4]/button')   # 登录页面提交登录按钮
    # 注册页面
    idx_register_btn = (By.CLASS_NAME, 'register__ONaWA fs14 ft5 m-r8')  # 首页注册按钮
    # 首页


    # 活动页面

    # 充值页面

    # 个人中心页面


    def click_idx_login_btn(self):
        self.click(self.idx_login_btn)

    def input_user_text(self, text):
        self.send_key(self.user_input_box, text)

    def input_psd_text(self, text):
        self.send_key(self.psd_input_box, text)

    def click_login_btn(self):
        self.click(self.login_btn)
