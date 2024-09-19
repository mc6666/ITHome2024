from operator import add, sub, mul, truediv

def perform1(func, a, b ):
    return func(a, b)

print(perform1(add, 100, 10))