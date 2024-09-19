import math

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def exp(a, b):
    return a**b

def log(a, b):
    return math.log(a, b)

def perform1(func, a, b ):
    return func(a, b)
    
if __name__ == "__main__":
    #  print(subtract(5, 10))
    print(perform1(subtract, 5, 10))
    print(perform1(log, 100, 10))
    