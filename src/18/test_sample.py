import pytest

# 測試函數
def func(x):
    return x + 1

# 測試案例
def test_answer():
    assert func(3) == 5
    
if __name__ == '__main__':
    print(func(2))