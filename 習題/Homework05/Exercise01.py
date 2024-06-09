import matplotlib.pyplot as plt
import numpy as np
import gd

# 資料
x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

# 線性預測函數
def predict(a, xt):
    return a[0].Value() + a[1].Value() * xt

# 均方誤差損失函數
def MSE(a, x, y):
    total = 0
    for i in range(len(x)):
        total += (y[i] - predict(a, x[i])) ** 2
    return total

# 優化時的損失函數
def loss(p):
    return MSE(p, x, y)

# 參數的初始猜測值
p = [gd.Value(0.0), gd.Value(0.0)]

# 執行梯度下降
plearn = gd.gradientDescendent(loss, p, max_loops=3000, dump_period=1)

# 繪製圖形
y_predicted = [predict(plearn, xt) for xt in x]
print('y_predicted=', y_predicted)
plt.plot(x, y, 'ro', label='原始數據')
plt.plot(x, y_predicted, label='擬合線')
plt.legend()
plt.show()