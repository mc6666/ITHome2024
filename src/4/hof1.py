from functools import reduce

# 測試資料
numbers = (1, 2, 3, 4)

# 連加
result = reduce(lambda x, y: x + y, numbers)
print(result)

# 連乘
result = reduce(lambda x, y: x * y, numbers)
print(result)

