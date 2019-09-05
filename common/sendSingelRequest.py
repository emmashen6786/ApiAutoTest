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


class SendSingelRequests:
    s = requests.session()

    def sendSingelRequests(self, apiData):
        if apiData == None:
            return "表格未填写数据"
        else:
            if apiData["switch"] == "Close":
                return
            else:
                try:
                    # 从读取的表格中获取响应的参数作为传递
                    serialNumber = apiData["serialNumber"]
                    apiName = apiData["apiName"]
                    method = apiData["method"]
                    url = apiData["url"]
                    if apiData["headers"] == "":
                        h = None
                    else:
                        h = apiData["headers"]

                    if apiData["params"] == "":
                        par = None
                    else:
                        par = eval(apiData["params"])

                    if apiData["body"] == "":
                        body_data = None
                    else:
                        body_data = eval(apiData["body"])

                    if apiData["files"] == "":
                        file_data = None
                    else:
                        file_data = eval(apiData["files"])

                    publice_params = apiData["dynamicParams"]

                    type = apiData["type"]

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
                        # print(resp.text)
                        return resp
                    except ReadTimeout:
                        response_data = {"result": "TimeOut"}
                        return response_data

                except Exception as e:
                    print(e)


if __name__ == '__main__':
    testData = ReadExcel("/Users/shuiguowei/Practice/BackEnd/ApiAutoTest/data/testdemo.xlsx", "Sheet1").readExcel()
    response = SendSingelRequests().sendSingelRequests(testData)
