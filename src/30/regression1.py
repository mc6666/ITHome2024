## 載入套件
import numpy as np 
from sklearn.datasets import make_regression

## 產生隨機資料100筆
X_org, y = make_regression(n_samples=100, n_features=1, noise=15, random_state=42)
X_org.shape, y.shape

# 設定 b 對應的 X，固定為 1
one=np.ones((X_org.shape[0], 1))
one.shape

one[:10]

# X 結合 b 對應的 X
X=np.concatenate((X_org, one), axis=1)
X.shape

## 估算簡單線性迴歸的參數(w、b)
beta = np.linalg.inv(X.T @ X) @ X.T @ y
print(beta)

## 驗算
beta  = np.polyfit(X_org.reshape(-1), y, deg=1)
print(beta)

## 顯示迴歸線
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
plt.scatter(X[:, 0], y)
plt.plot(X[:, 0], X[:, 0] * beta[0] + beta[1], 'r');
plt.show()
