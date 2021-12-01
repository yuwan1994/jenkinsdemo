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
import time
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from sys import platform

if __name__ == '__main__':
    print('使用pycharm链接demo进行开发')
    print('开始测试')
    response = requests.get('https://www.baidu.com')
    print(response.content)
    service = None
    if platform == "darwin":
        service = Service(r'chromedriver95')
    elif platform == "win32":
        service = Service(r'chromedriver96.45.exe')
    else:
        print(f'{platform}')
    browser = Chrome(service=service)
    browser.get('https://www.baidu.com')
    browser.get('https://www.sina.com')
    browser.save_screenshot('shot.png')
    time.sleep(5)
    print('访问结束')
    browser.quit()
