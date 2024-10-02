# 階層(factorial )計算
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))
    
def add_or_multiply(operator):
    if operator == '*':
        return 5 * 6
    else:
        return 5 + 6
