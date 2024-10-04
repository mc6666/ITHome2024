from functools import reduce, lru_cache
import timeit
    
# 階層(factorial)計算
@lru_cache
def factorial(n):
    total=1
    while(n>0):
        total=total*n
        n=n-1
    return total    

if __name__ == '__main__':
    # 執行測試
    n = 1000
    factorial(n)

    # run again
    factorial(n)

    print(factorial.cache_info())
