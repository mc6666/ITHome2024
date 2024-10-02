# 階層(factorial )計算
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))