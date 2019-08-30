# coding:utf-8
import unittest

def all_case():
# 待执行用例的目录
    case_dir = "C:\\Users\张羽飞\Desktop\py_discover\case"
    # testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                               pattern="test*.py",
                                               top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    # for test_suite in discover:
    #     for test_case in test_suite:
    #     # 添加用例到testcase
    #     testcase.addTests(test_case)
    # print(discover)
    return discover
if __name__ == "__main__":
    # 返回实例
    # runner = unittest.TextTestRunner()
    import HTMLTestRunner
    # my_report = "C:\\Users\张羽飞\Desktop\py_discover\case\report\result.html"
    fp = open("C:\\Users\\张羽飞\\Desktop\\py_discover\\case\\report\\result.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='接口测试执行结果',
        description='用例执行结果'
    )
    # run所有用例
    runner.run(all_case())
    fp.close()

