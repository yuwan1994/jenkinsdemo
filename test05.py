#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : test05.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 
@Modify Time @Author @Version @Description
------------ ------- -------- -----------
2021/12/6 3:43 下午 yuwan  1.0  None
"""
import allure
import pytest


datas = [
    {"user": "king", "pwd": 123456},
    {"user": "king1", "pwd": 1234567},
    {"user": "hello", "pwd": 123456}
]


@pytest.mark.parametrize("data", datas)
def test_login(data):
    print(data)
    assert data["user"].startswith("king") and data["pwd"] == 123456


@pytest.mark.parametrize("data", datas, ids=["正确的用户名和密码", "正确的用户名和错误的密码", "不存在的用户名和密码"])
def test_login2(data):
    print(data)
    assert data["user"].startswith("king") and data["pwd"] == 123456


if __name__ == '__main__':
    pass
