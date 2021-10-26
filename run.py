#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : run.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 
@Modify Time @Author @Version @Desciption
------------ ------- -------- -----------
2021/10/26 4:20 下午 yuwan  1.0  None
"""
import unittest
from unittest.runner import TextTestRunner, TextTestResult
from testcase.testdriver import Baidu

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Baidu('test_baidu'))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
