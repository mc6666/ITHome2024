def add(*arg):
    total = 0
    for i in arg:
        total += i
    return total

def multiply(*arg):
    total = 1
    for i in arg:
        total *= i
    return total

def perform1(func, *arg):
    return func(*arg)
    
if __name__ == "__main__":
    print(perform1(multiply, 1, 10, 20))
    