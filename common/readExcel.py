#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site:
@software: PyCharm
@file: readExcel.py
@time: 2018/3/24 9:37
"""
import xlrd


class ReadExcel:
    def __init__(self, path, sheet_name):
        self.path = path
        self.data = xlrd.open_workbook(path)
        self.table = self.data.sheet_by_name(sheet_name)

    def readExcel(self):
        # 获取总行数、总列数
        nrows = self.table.nrows
        ncols = self.table.ncols
        if nrows > 1:
            # 获取第一列的内容，列表格式
            keys = self.table.row_values(0)
            # print(keys)

            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, nrows):
                values = self.table.row_values(col)
                # keys，values这两个列表一一对应来组合转换为字典
                api_dict = dict(zip(keys, values))
                # print(api_dict)
                listApiData.append(api_dict)

            return listApiData
        else:
            print("表格未填写数据")
            return None


if __name__ == '__main__':
    path = "/Users/shuiguowei/Practice/BackEnd/ApiAutoTest/data/testdemo.xlsx"
    sheet_name = "Sheet1"
    s = ReadExcel(path, sheet_name).readExcel()
