# 宣告Decorator類別
class Counter:
    def __init__(self, func): # 初始化
        self.func = func
        self.count = 0 # 記錄Decorator被呼叫的次數

    def __call__(self, *args, **kwargs): # 
        self.count += 1 # 被呼叫的次數 + 1
        print(f"被呼叫的次數：{self.count}")
        return self.func(*args, **kwargs)

@Counter
def greet(name):
    print(f"Hello {name}!")

# 測試
greet("Alice")
greet("Michael") 