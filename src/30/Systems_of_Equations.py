import numpy as np

a = np.array([[1, 2, 3], [3, 2, 1], [3, 1, 2]])
b = np.array([14, 10, 11])
print('method 1\n', np.linalg.inv(a) @ b)
# 驗證
print('method 2\n', np.linalg.solve(a, b))
