# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 生成合成數據集（模擬廣告支出與銷售量的關係）
np.random.seed(42)

# 假設我們有3種不同的廣告渠道（TV、Radio、Newspaper）的支出，目標是預測銷售量
data_size = 200
TV = np.random.uniform(10, 300, data_size)  # TV廣告費用
Radio = np.random.uniform(5, 50, data_size)  # Radio廣告費用
Newspaper = np.random.uniform(1, 30, data_size)  # 報紙廣告費用

# 模擬銷售量（加入了一些隨機噪音）
Sales = 3.5 + 0.05 * TV + 0.1 * Radio + 0.02 * Newspaper + np.random.normal(0, 2, data_size)

# 創建數據框
df = pd.DataFrame({
    'TV': TV,
    'Radio': Radio,
    'Newspaper': Newspaper,
    'Sales': Sales
})

# 顯示數據集的前5行
print(df.head())

# 分割數據集為訓練集和測試集
X = df[['TV', 'Radio', 'Newspaper']]  # 特徵矩陣
y = df['Sales']  # 目標變量

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 創建並訓練線性迴歸模型
model = LinearRegression()
model.fit(X_train, y_train)

# 預測銷售量
y_pred = model.predict(X_test)

# 模型的參數（係數和截距）
print("模型係數：", model.coef_)
print("模型截距：", model.intercept_)

# 評估模型的性能
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"均方誤差 (MSE): {mse:.2f}")
print(f"R平方值 (R2 score): {r2:.2f}")

# 視覺化實際銷售量和預測銷售量
plt.scatter(y_test, y_pred)
plt.xlabel("實際銷售量")
plt.ylabel("預測銷售量")
plt.title("實際銷售量 vs 預測銷售量")
plt.show()
