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
from os import system
from sys import argv
from pytest import main
from createjenkinsenvxml import *
from source import root_path
from requests import get


if __name__ == '__main__':
    print('使用pycharm链接demo进行开发')
    print('开始测试')
    # response = requests.get('https://www.baidu.com')
    # print(response.content)
    # service = None
    # if platform == "darwin":
    #     service = Service(r'chromedriver95')
    # elif platform == "win32":
    #     service = Service(r'chromedriver96.45.exe')
    # else:
    #     print(f'{platform}')
    # browser = Chrome(service=service)
    # browser.get('https://www.baidu.com')
    # # browser.save_screenshot('shot.png')
    # time.sleep(5)
    # browser.quit()
    resultpath = '/resultspath'
    file_path = root_path / f'{resultpath}/environment.xml'
    create_xml(file_path, {'platform': 'Windows', 'Python.Version': '3.10.0', 'pytest.Version': '6.2.4',
               'allure-pytest.Version': '2.9.43', 'project': 'jenkinsdemo', 'user': 'yuwan'})
    tree = ET.parse(file_path)  # 解析result.xml这个文件
    root = tree.getroot()
    pretty_xml(root, '\t', '\n')  # 执行美化方法
    tree.write(file_path, encoding='utf-8')
    main(['-s', '--alluredir', resultpath])
    # system('allure generate jsondir -c -o report')
