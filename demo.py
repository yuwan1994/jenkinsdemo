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

if __name__ == '__main__':
    print('使用pycharm链接demo进行开发')
    print('测试步骤')
    response = requests.get('https://www.baidu.com')
    print(response.text)
