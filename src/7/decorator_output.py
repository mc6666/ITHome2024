def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("呼叫函數前")
        output = func(*args, **kwargs)
        print("呼叫函數後")
        return output
    return wrapper

@log_decorator
def add(a, b):
    return a + b
    
# 呼叫 add
print(add(1, 2))