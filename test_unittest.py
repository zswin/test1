# coding=utf-8
__author__ = 'zs'

import unittest

class TestAvg(unittest.TestCase):
    def test_int(self):
        print('testing  integer')
        self.assertEqual((1+35)/2, 18)
    def test_floag(self):
        print('testing float')
        self.assertEqual((1.5+2.5)/2, 2.0)
if __name__ == '__main__':
    unittest.main()