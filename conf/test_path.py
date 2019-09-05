import os

global_path_vars = {
    'testdemo_01': '/Users/shuiguowei/Practice/BackEnd/ApiAutoTest/data/testdemo.xlsx',
    'testapplication': '/Users/shuiguowei/Practice/BackEnd/ApiAutoTest/data/testapplication.xlsx'
}

# get path variables or use the default settings
path1 = os.path.abspath(global_path_vars['testdemo_01'])
path2 = os.path.abspath(global_path_vars['testapplication'])
