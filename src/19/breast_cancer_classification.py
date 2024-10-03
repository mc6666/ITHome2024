# Import required libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 加载乳腺癌威斯康辛数据集
data = load_breast_cancer()

# 将数据集转换为DataFrame以便更好地观察
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# 输出数据集的信息
print("數據集維度：", df.shape)
print("數據集的前5行：\n", df.head())

# 分割数据集为训练集和测试集
X = df.drop(columns=['target'])  # 特征
y = df['target']  # 目标

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 建立随机森林分类器
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 训练模型
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 评估模型
accuracy = accuracy_score(y_test, y_pred)
print(f"模型的準確度: {accuracy * 100:.2f}%")

# 顯示分類報告和混淆矩陣
print("分類報告：\n", classification_report(y_test, y_pred))
print("混淆矩陣：\n", confusion_matrix(y_test, y_pred))
