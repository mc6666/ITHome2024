# 宣告Decorator函數
def log_decorator(func):
    # inner function
    def wrapper(): 
        print("呼叫函數前")
        func()
        print("呼叫函數後")
    # 呼叫 inner function
    return wrapper

# 為 say_hello 函數加上 Decorator
@log_decorator
def say_hello():
    print("hello !")
    
# 呼叫 say_hello
say_hello()    