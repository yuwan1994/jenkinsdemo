#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : test02.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 
@Modify Time @Author @Version @Description
------------ ------- -------- -----------
2021/12/3 4:27 下午 yuwan  1.0  None
"""
import allure
from pytest import main


@allure.step("第一步")
def passing_step():
    pass


@allure.step("第二步")
def step_with_nested_steps():
    nested_step()


@allure.step("第三步")
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step("第四步{0}，{arg2}")
def nested_step_with_arguments(arg1, arg2):
    pass


@allure.step("第五步")
def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()


if __name__ == '__main__':
    main()
