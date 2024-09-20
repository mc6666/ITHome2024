# 宣告Decorator函數
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3) # 3 會對應 times
def greet(name): # name 會對應 *args
    print(f"Hello {name}!")

greet("Michael") 