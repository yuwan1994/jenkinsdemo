#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : basedriver.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 
@Modify Time @Author @Version @Desciption
------------ ------- -------- -----------
2021/10/26 4:21 下午 yuwan  1.0  None
"""
from selenium.webdriver import Chrome


class Driver:
    driver = Chrome()
    driver.implicitly_wait(10)


if __name__ == '__main__':
    pass
