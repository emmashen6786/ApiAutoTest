import unittest
from testcase.case_01 import Test_api

# suite = unittest.TestSuite()  # 建立测试套件
# cases = []
# for k in Test_api.__dict__:
#     if k.startswith("test_borrower_info_api") or k.startswith("test_application_api"):
#         cases.append(Test_api(k))
# suite.addTests(cases)

if __name__ == '__main__':
    # 通过使用testloade中封装的方法实现批量新增用例与执行用例
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Test_api)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
