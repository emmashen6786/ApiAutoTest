# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: emmashen
@site:
@software: PyCharm
@file: sendRequests.py
@time: 2019/8/26 11:40
"""
from common.readExcel import ReadExcel
import requests
import json
from common.requester import Requester
from common.getJWT import GetJWT
from requests import ReadTimeout


class SendRequests:
    s = requests.session()

    def sendRequests(self, apiData):
        if apiData == None:
            return "表格未填写数据"
        else:
            reContent = []

            for rowIndex in range(len(apiData)):
                if apiData[rowIndex]["switch"] == "Close":
                    continue
                else:
                    try:
                        # 从读取的表格中获取响应的参数作为传递
                        serialNumber = apiData[rowIndex]["serialNumber"]
                        apiName = apiData[rowIndex]["apiName"]
                        method = apiData[rowIndex]["method"]
                        url = apiData[rowIndex]["url"]
                        if apiData[rowIndex]["headers"] == "":
                            h = None
                        else:
                            h = apiData[rowIndex]["headers"]

                        if apiData[rowIndex]["params"] == "":
                            par = None
                        else:
                            par = eval(apiData[rowIndex]["params"])

                        if apiData[rowIndex]["body"] == "":
                            body_data = None
                        else:
                            body_data = eval(apiData[rowIndex]["body"])

                        if apiData[rowIndex]["files"] == "":
                            file_data = None
                        else:
                            file_data = eval(apiData[rowIndex]["files"])

                        publice_params = apiData[rowIndex]["dynamicParams"]

                        type = apiData[rowIndex]["type"]

                        if type == "json":
                            body = json.dumps(body_data)
                        if type == "data":
                            body = body_data
                        else:
                            body = body_data

                        h = eval(h) if isinstance(h, str) else h
                        h["Authorization"] = GetJWT().getJWT()

                        requester = Requester(method, url, h, par, body, file_data, publice_params)
                        try:
                            if method == "post":
                                resp = requester.setPost(self.s)
                            elif method == "put":
                                resp = requester.setPut(self.s)
                            elif method == "get":
                                resp = requester.setGet(self.s)
                            else:
                                response_data = {"result": "ERROR"}
                                return response_data
                            reContent.append(resp.text)

                        except ReadTimeout:
                            response_data = {"result": "TimeOut"}
                            return response_data

                    except Exception as e:
                        print(e)
            print(reContent)
            return reContent


if __name__ == '__main__':
    testData = ReadExcel("/Users/shuiguowei/Practice/BackEnd/ApiAutoTest/data/testdemo.xlsx", "Sheet1").readExcel()
    response = SendRequests().sendRequests(testData)
