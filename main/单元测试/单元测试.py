"""
@author Lucas
@date 2018/11/27 21:54

"""

import unittest

from main.单元测试.被测试的代码 import mySum


class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试时调用")

    def tearDown(self):
        print("结束测试时调用")

    # 为了测试mySum
    def test_mySum(self):
        self.assertEqual(mySum(1, 2), 3, "加法有误")


if __name__ == '__main__':
    unittest.main()
