# coding:utf-8
import unittest
import time
class Test_04(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        time.sleep(1)
        print("end")
    def test_04(self):
        print("执行用例4")
if __name__ == "__main__":
    unittest.main()
