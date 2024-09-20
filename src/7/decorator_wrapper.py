from functools import wraps

def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        """wrapper documentation"""
        print(f"----- {function.__name__}: start -----")
        output = function(*args, **kwargs)
        print(f"----- {function.__name__}: end -----")
        return output
    return wrapper

@logger
def add_two_numbers(a, b):
    """this function adds two numbers"""
    return a + b
    
print(add_two_numbers.__name__)
print(add_two_numbers.__doc__)