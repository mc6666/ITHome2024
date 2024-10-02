import pytest
import sys, os

# 將路徑加入環境變數
sys.path.append(os.path.abspath(".."))

# 引用 main_program 資料夾的factorial函數
from src import factorial

class TestMath():
    def test_factorial(self):
        # 測試階層計算是否正確
        assert factorial(5) == 1*2*3*4*5