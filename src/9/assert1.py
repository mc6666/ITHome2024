def divide(a, b):
    assert (b != 0), f"{b}不可為0 !!"
    result = a / b
    return result
    
if __name__ == '__main__':
    divide(1, 0)