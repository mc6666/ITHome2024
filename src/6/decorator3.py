import time, inspect

# 宣告Decorator函數
def log_decorator(func):
    # inner function
    def wrapper(*arg1, **arg2): 
        # print("呼叫函數前")
        start_time = time.time()
        func(*arg1, **arg2)
        print(f"【{func.__name__}】執行時間：{(time.time() - start_time)} 秒")        
        print(f"\t參數：", end=' ') # {inspect.signature(func)}: {arg1}")
        for name, value in zip(inspect.signature(func).parameters.keys(), arg1):
            print(f"{name}:{value}", end='\t')
            
        print(f"\t\t")        
        # print("呼叫函數後")
    # 呼叫 inner function
    return wrapper

@log_decorator
def func_a(x):
    print("hello a!")
    
@log_decorator
def func_b(x1, x2):
    total = 0
    for i in range(100_001):
        total += i
    print("hello b!")

@log_decorator
def func_c(y1, y2, y3):
    print("hello c!")
    
if __name__ == "__main__":
    func_a(1)
    func_b(2, 3)
    func_c(4, 5, 6)
    