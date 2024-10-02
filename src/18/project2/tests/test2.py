import unittest, sys, os

# 將路徑加入環境變數
sys.path.append(os.path.abspath(".."))

# 引用 main_program 資料夾的factorial函數
from main_program import *

class TestMath(unittest.TestCase):
    def test_factorial(self):
        # 測試階層計算是否正確
        self.assertEqual(factorial(5), 1*2*3*4*5)

    def test_add_or_multiply(self):
        self.assertEqual(add_or_multiply('*'), 5*6)

if __name__ == '__main__':
    unittest.main()