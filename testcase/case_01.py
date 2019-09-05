#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: emmashen
@site:
@software: PyCharm
@file: case_01.py
@time: 2019/8/28 10:58
"""
import unittest
import requests
import ddt
from common.sendSingelRequest import SendSingelRequests
from common.readExcel import ReadExcel
import os
from conf import test_path
import json

# 配置文件里读取表格数据
Data = ReadExcel(test_path.path1, "Sheet1").readExcel()
ApplicatonData = ReadExcel(test_path.path2, "Sheet1").readExcel()


@ddt.ddt
class Test_api(unittest.TestCase):
    """测试框架使用Unittest和DDT相结合的方式"""

    def setUp(self):
        pass
        # print("测试前环境与数据准备")

    # @ddt.data(*Data)
    # def test_ddt(self, data):
    #     print(data)

    @ddt.data(*Data)
    # @ddt.unpack
    def test_borrower_info_api(self, data):
        actual_result = SendSingelRequests().sendSingelRequests(data).text
        # print(actual_result)
        expect_result = data["expect_result"]
        # print(expect_result)
        self.assertEqual(expect_result, actual_result, "接口返回与预期不一致，实际结果是%s" % actual_result)

    @ddt.data(*ApplicatonData)
    def test_application_api(self, data):
        actual_result = SendSingelRequests().sendSingelRequests(data)
        if actual_result.status_code in (200,201):
            actual_result = json.loads(actual_result)
            actual_judge_file = str(actual_result["loanAppId"])

            # print(actual_judge_file)
            expect_result = data["expect_result"]
            expect_result = json.loads(expect_result)
            expect_judge_file = str(expect_result["loanAppId"])
            # print(expect_judge_file)

            self.assertIn(expect_judge_file, actual_judge_file, "接口返回与预期不一致，实际结果是%s" % actual_result)
        else:
            actual_status = actual_result.status_code
            expect_status = 200
            self.assertEqual(expect_status, actual_status, "接口有问题，详情是%s" % actual_result)

    def tearDown(self):
        pass
        # print("测试完成后的环境与数据清理")


if __name__ == '__main__':
    unittest.main()
