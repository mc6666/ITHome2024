import math

add = lambda a, b: a+b
subtract = lambda a, b: a-b
multiply = lambda a, b: a*b
divide = lambda a, b: a/b
exp = lambda a, b: a**b
log = lambda a, b: math.log(a, b)

def perform1(func, a, b ):
    return func(a, b)
    
if __name__ == "__main__":
    #  print(subtract(5, 10))
    print(perform1(subtract, 5, 10))
    print(perform1(log, 100, 10))
    print(perform1(lambda a, b: math.log(a, b), 1000, 10))
    