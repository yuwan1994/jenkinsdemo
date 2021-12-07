#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : createjenkinsenvxml.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 
@Modify Time @Author @Version @Description
------------ ------- -------- -----------
2021/12/6 4:36 下午 yuwan  1.0  None
"""
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree import ElementTree


def create_xml(file_path, contents):
    """
    根据生成xml文件
    @param file_path:
    @type file_path:
    @param contents:要显示的内容
    @type contents:dict
    @return:
    @rtype:
    """
    from xml.etree.ElementTree import ElementTree
    environment = Element('environment')  # 生成environment根节点
    for content in contents:
        parameter = SubElement(environment, 'parameter')  # 生成environment节点的子节点parameter
        key = SubElement(parameter, 'key')  # 生成parameter节点的子节点key
        key.text = content
        value = SubElement(parameter, 'value')  # 生成root节点的第二个子节点value
        value.text = contents[content]
    element_tree = ElementTree(environment)
    # 文件头部添加<?xml version="1.0" encoding="GBK"?>，添加参数xml_declaration=True
    element_tree.write(file_path, encoding='utf-8')
    # element_tree.write(file_path, encoding='utf-8', xml_declaration=True)


# element为传进来的Element类，参数'\t用于缩进，'\n用于换行
def pretty_xml(element, indent, newline, level=0):
    """
    美化xml文件
    @param element:根节点
    @type element:Element
    @param indent:/t是水平制表符跳到下一个TAB位置
    @type indent:str
    @param newline:要添加的转义字符 ，/n换行符
    @type newline:str
    @param level:
    @type level:
    @return:
    @rtype:
    """
    # 判断element是否有子元素
    if element:
        # 如果element的text没有内容
        if element.text is None or element.text.isspace():
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # 此处两行如果把注释去掉，Element的text也会另起一行
    # else:
    # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    element_list = list(element)  # 将element转成list
    for sub_element in element_list:
        # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
        if element_list.index(sub_element) < (len(element_list) - 1):
            sub_element.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
            sub_element.tail = newline + indent * level
            # 对子元素进行递归操作
        pretty_xml(sub_element, indent, newline, level=level + 1)


if __name__ == '__main__':
    create_xml('result.xml', {'platform': 'Windows', 'Python.Version': '3.10.0', 'pytest.Version': '6.2.4',
               'allure-pytest.Version': '2.9.43', 'project': 'jenkinsdemo', 'user': 'yuwan'})
    tree = ElementTree.parse('result.xml')  # 解析result.xml这个文件
    root = tree.getroot()
    pretty_xml(root, '\t', '\n')  # 执行美化方法
    tree.write('result.xml', encoding='utf-8')
