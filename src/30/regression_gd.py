import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from sklearn.datasets import make_regression
import numpy as np

# 學習率
LEARNING_RATE=0.005
# 損失函數與前一次的差異設定值，小於設定值，就停止
ERROR_TOLERENCE=0.01
# 圖形更新的頻率
PAUSE_INTERVAL=0.5

# 產生圖形大小
fig, ax = plt.subplots()
fig.set_size_inches(8, 6)

# 產生隨機資料
X, y= make_regression(n_samples=200, n_features=1, noise=5, bias=50)
X=X.ravel()
# print(X, y)            
plt.scatter(X,y)
line, = ax.plot(X, [0] * len(X), 'r')

# 隨機指定權重(Weights)及偏差(Bias)
b0 = np.random.rand()
b1 = np.random.rand()

# 求預測值(Y hat)
def calc_forecast(b0, b1, x):
    return b0 + (b1*x) 

# 計算損失函數 MSE
def calc_loss(b0, b1, X, y):
    lossValue = 0
    # MSE   
    for (xi, yi) in zip(X, y):
        # print(type(b0), type(b1), type(xi))        
        lossValue += 0.5 * ((calc_forecast(b0, b1, xi) - yi)**2)
    return lossValue

# 偏微分，求梯度
def derivatives(b0, b1, X, y):
    b0_offset = 0
    b1_offset = 0
    for (xi, yi) in zip(X, y):
        b0_offset += calc_forecast(b0, b1, xi) - yi
        b1_offset += (calc_forecast(b0, b1, xi) - yi)*xi

    b0_offset /= len(X)
    b1_offset /= len(X)

    return b0_offset, b1_offset

# 更新權重
def updateParameters(b0, b1, X, y, alpha):
    b0_offset, b1_offset = derivatives(b0, b1, X, y)
    b0 = b0 - (alpha * b0_offset)
    b1 = b1 - (alpha * b1_offset)

    return b0, b1
 

# 主程式
i=0
prev_loss = 999999999999.
while True:
    if i % 100 == 0:
        # 更新圖形Y軸資料
        y_new = [b0 + b1 * xplot for xplot in X]
        line.set_data(X, y_new)  # update the data.
        #ax.cla()
        plt.pause(PAUSE_INTERVAL)
    current_loss = calc_loss(b0, b1, X, y)
    # print('current_loss=',current_loss)
    # print(prev_loss - current_loss)
    if prev_loss - current_loss > ERROR_TOLERENCE:
        b0, b1 = updateParameters(b0, b1, X, y, LEARNING_RATE)
        prev_loss = current_loss
        # print('prev_loss=',prev_loss)
    else:
        print(b0, b1)
        break
    i+=1

plt.show()