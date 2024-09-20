import time

# 宣告Decorator函數
def log_decorator(func):
    # inner function
    def wrapper(): 
        # print("呼叫函數前")
        start_time = time.time()
        func()
        print(f"【{func.__name__}】 執行時間：{(time.time() - start_time)} 秒")        
        # print("呼叫函數後")
    # 呼叫 inner function
    return wrapper

@log_decorator
def func_a():
    print("hello a!")
    
@log_decorator
def func_b():
    total = 0
    for i in range(100_001):
        total += i
    print("hello b!")

@log_decorator
def func_c():
    print("hello c!")
    
if __name__ == "__main__":
    func_a()
    func_b()
    func_c()
    