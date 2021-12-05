#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : test03.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 用了 allure.attach() 来插入一段自己写的HTML和 allure.attach.file() 来导入一个已存在的HTML文件（pytest-html报告）
@Modify Time @Author @Version @Description
------------ ------- -------- -----------
2021/12/3 4:35 下午 yuwan  1.0  None
"""
import pytest
import allure
import os


@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('在fixture前置操作里面添加一个附件txt', 'fixture前置附件', allure.attachment_type.TEXT)

    def finalizer_module_scope_fixture():
        allure.attach('在fixture后置操作里面添加一个附件txt', 'fixture后置附件', allure.attachment_type.TEXT)

    request.addfinalizer(finalizer_module_scope_fixture)


def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_fixture_with_finalizer):
    pass


def test_multiple_attachments():
    allure.attach('<head></head><body> 一个HTML页面 </body>', 'Attach with HTML type', allure.attachment_type.HTML)
    allure.attach.file('./report/index.html', '插入一个html文件', attachment_type=allure.attachment_type.HTML)


if __name__ == '__main__':
    pytest.main(['--alluredir', 'test03json'])
    os.system('allure generate ./test03json -o ./test03jsonreport')
