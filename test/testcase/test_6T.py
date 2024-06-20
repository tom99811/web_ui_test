#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

from test.page.sixTPage import SixTSport
from test.testcase.case_modle import *
from data.config import Config

sys.path.append('../')
c = Config()


class SixTBase(Model):

    def test_sixT(self):
        SixT = SixTSport(self.driver)
        logger.info("开始执行登录操作")
        SixT.click_idx_login_btn()  # 点击首页登录按钮
        SixT.input_user_text(c.get('user', 'username'))
        SixT.input_psd_text(c.get('user', 'password'))
        SixT.click_login_btn()
        self.assertIn('6T体育', self.driver.title)
        time.sleep(5)


if __name__ == '__main__':
    s = SixTBase()
    s.test_sixT()
