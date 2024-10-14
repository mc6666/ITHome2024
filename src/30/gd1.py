import numpy as np
import matplotlib.pyplot as plt

# 目標函數(損失函數):y=x^2
def func(x): return x ** 2 #np.square(x)

# 目標函數的一階導數:dy/dx=2*x
def dfunc(x): return 2 * x

# 梯度下降
# x_start: x的起始點
# df: 目標函數的一階導數
# epochs: 執行週期
# lr: 學習率
def GD(x_start, df, epochs, lr):    
    xs = np.zeros(epochs+1)    
    w = x_start    
    xs[0] = w    
    for i in range(epochs):         
        dx = df(w)        
        # 權重的更新 W_new = W — learning_rate * gradient        
        w += - dx * lr         
        xs[i+1] = w    
    return xs

# 超參數(Hyperparameters)
x_start = 5     # 起始權重
epochs = 15     # 執行週期數 
lr = 0.3        # 學習率 

# 梯度下降法 
# *** Function 可以直接當參數傳遞 ***
w = GD(x_start, dfunc, epochs, lr=lr) 
print (np.around(w, 2))
# 輸出：[-5.     -2.     -0.8    -0.32   -0.128  -0.0512]

color = 'r'    
from numpy import arange
t = arange(-6.0, 6.0, 0.01)
plt.plot(t, func(t), c='b')
plt.plot(w, func(w), c=color, label='lr={}'.format(lr))    
plt.scatter(w, func(w), c=color, ) 

# 設定中文字型
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\msjhbd.ttc", size=20)   
# 矯正負號
plt.rcParams['axes.unicode_minus'] = False

plt.title('梯度下降法', fontproperties=font)
plt.xlabel('w', fontsize=20)
plt.ylabel('Loss', fontsize=20)

plt.show()