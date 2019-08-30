# coding:utf-8
import unittest
import time
class Test_01(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        time.sleep(1)
        print("end")
    def test_01(self):
        print("执行用例1")
if __name__ == "__main__":
    unittest.main()
