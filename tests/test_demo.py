# -*- coding: utf-8 -*-
"""
@Projcet :  python-learning
@File : test_demo
@Descriptioin : 
@DateTime : 2020/10/30 10:46
@Author : fangqing.fan#hotmail.com
"""


import unittest
import sys

from sample.Demo import add_one


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)
        print(add_one(5))


if __name__ == '__main__':
    unittest.main()