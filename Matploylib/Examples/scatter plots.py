import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
# 利用反正切（arctan2的正切角是原点与（1,0）点的射线和原点与（y，x）的射线的夹角）来产生-1到1的随机数，应用到下面scatter的color参数中
T = np.arctan2(Y, X)

plt.axes([0.025, 0.025, 0.95, 0.95])
# scatter()方法中s为散点的大小，c为散点的颜色，alpha为透明度
plt.scatter(X, Y, s=75, c=T, alpha=0.5)
plt.xlim(-1.5, 1.5), plt.xticks([])
plt.ylim(-1.5, 1.5), plt.yticks([])
plt.show()
