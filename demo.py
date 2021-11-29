#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : demo.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 
@Modify Time @Author @Version @Description
------------ ------- -------- -----------
2021/11/19 5:09 下午 yuwan  1.0  None
"""
import requests
from selenium.webdriver import Chrome

if __name__ == '__main__':
    print('使用pycharm链接demo进行开发')
    print('开始测试')
    response = requests.get('https://www.baidu.com')
    print(response.content)
    browser = Chrome(executable_path='chromedriver95')
    browser.get('https://www.baidu.com')
    browser.quit()

