import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
# [X,Y] = meshgrid(x,y) 将向量x和y定义的区域转换成矩阵X和Y
# 其中矩阵X的行向量是向量x的简单复制，而矩阵Y的列向量是向量y的简单复制
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
ax.set_zlim(-2, 2)

# savefig('../figures/plot3d_ex.png',dpi=48)
plt.show()
