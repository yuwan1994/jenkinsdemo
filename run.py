#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : run.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 
@Modify Time @Author @Version @Description
------------ ------- -------- -----------
2021/12/9 9:45 上午 yuwan  1.0  None
"""
from requests import get

if __name__ == '__main__':
    get('http://120.25.162.206:8080//job/demo02/buildWithParameters?token=isatoken')    # 触发构建请求
