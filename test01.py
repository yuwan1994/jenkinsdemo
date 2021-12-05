#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : test01.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 
@Modify Time @Author @Version @Description
------------ ------- -------- -----------
2021/12/3 2:19 下午 yuwan  1.0  None
"""
import allure
from pytest import main
import os


# @allure.title('这是标题')
# @allure.step('这是步骤')
# @allure.id('这是id')
# @allure.description('这是描述')
# @allure.feature('这是特征')
# @allure.story('这是故事')
# @allure.tag('这是标签')
# def test_01():
#     assert 1
#
#
# @allure.description('这是描述02')
# @allure.step('这是步骤02')
# @allure.feature('这是详情02')
# def test_02():
#     test_01()
#     assert 1 == 1, '搜索失败'


@allure.epic('SaaS系统')
@allure.feature("测试登陆功能")
class Test1:
    @allure.story('测试登陆成功的场景')
    def test_1(self):
        assert 1 == 1

    @allure.story("测试登陆失败的场景")
    def test_2(self):
        assert 1 == 2


@allure.epic('SaaS系统')
@allure.feature("测试订单功能")
class Test2:
    @allure.story('测试下单成功的场景')
    def test_1(self):
        with allure.step('步骤1，浏览网页'):
            print(1)
        with allure.step('步骤2，添加购物车'):
            print(2)
        assert 1 == 1

    @allure.story("测试下单失败的场景")
    def test_2(self):
        assert 1 == 2


@allure.feature("测试物流功能")
class Test3:
    @allure.story('测试物流查询成功的场景')
    def test_1(self):
        assert 1 == 1


# class Test4:
#     @allure.severity("minor")
#     def test_1(self):
#         assert 1 == 1
#
#     @allure.severity("critical")
#     def test_2(self):
#         assert 1 == 2
#
#     @allure.severity("normal")
#     def test_3(self):
#         assert 3 == 3




if __name__ == '__main__':
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    main(['--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report')
