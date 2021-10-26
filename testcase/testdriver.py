#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : testdriver.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 
@Modify Time @Author @Version @Desciption
------------ ------- -------- -----------
2021/10/26 4:28 下午 yuwan  1.0  None
"""
from selenium.webdriver import Chrome
from unittest import TestCase
from pathlib import Path

root_path = Path(__file__).resolve().parent.parent
chrome_path = str(root_path / 'chromedriver95')


class Baidu(TestCase):

    def setUp(self) -> None:
        self.url = 'https://www.baidu.com'
        self.driver = Chrome(executable_path=chrome_path)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_baidu(self):
        self.driver.get(self.url)

if __name__ == '__main__':
    pass
