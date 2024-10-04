from functools import reduce, cache
import timeit
    
# 階層(factorial)計算
@cache
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))    

if __name__ == '__main__':
    # 執行測試
    n = 100_000
    print(
    timeit.timeit(
        "factorial(n)",
        globals=globals(),
        number=1
        )
    )

    # run again
    print(
    timeit.timeit(
        "factorial(n)",
        globals=globals(),
        number=1
        )
    )

    print(factorial.cache_info())
