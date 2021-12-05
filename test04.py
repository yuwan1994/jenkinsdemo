#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : test04.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 
@Modify Time @Author @Version @Description
------------ ------- -------- -----------
2021/12/3 5:21 下午 yuwan  1.0  None
"""
import allure
import pytest


# 链接测试
@allure.link('https://docs.pytest.org/en/latest',name='pytest帮助文档')
@allure.issue('http://baidu.com', name='点击我跳转百度')
@allure.testcase('http://bug.com/user-login-Lw==.html', name='点击我跳转禅道')
def test_other1():
    """测试链接，测试链接 ，测试链接"""
    pass



@allure.description('这是一个测试case')
@allure.title('test_other2的标题手动修改显示')
def test_other2():
    """测试链接，测试链接 ，测试链接"""
    pass


@pytest.mark.parametrize('param1', ['full', 'lisa'])
def test_other3(param1):
    print('param1 = ' + param1)
    pass






if __name__ == '__main__':
    pass
