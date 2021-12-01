#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : wechatnotice.py
@Contact : woshiyuwan@gmail.com
@License : (C)Copyright 2020-2021
@introduction : 实现企业微信通知
@Modify Time @Author @Version @Description
------------ ------- -------- -----------
2021/12/1 9:52 上午 yuwan  1.0  None
"""
import requests
import json
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class InformRobot:
    def __init__(self, webhook):  # webhook地址
        self.url = webhook
        self.sess = requests.session()

    def markdown_robot(self, jobname, job_url):
        data = {
            "msgtype": "markdown",  # 消息类型，此时固定为markdown
            "markdown": {
                "content": f"任务{jobname}构建开始！ \n" +
                           f'查看链接: [{job_url}]({job_url})。 \n' +
                           f"负责人：@所有人  \n" +
                           f'用户名：test01， 密码：test01'
            }
        }

        re_post = self.sess.post(self.url, data=json.dumps(data), verify=False)
        print(re_post.content, data)


if __name__ == "__main__":
    jobname = sys.argv[1]
    job_url = sys.argv[2]
    InformRobot('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=702df320-43fb-4e4a-953d-879ebfe315ac').markdown_robot(jobname, job_url)
