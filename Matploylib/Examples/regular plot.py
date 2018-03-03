import matplotlib.pyplot as plt
import numpy as np

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

# 添加子图，里面的数组提供图形大小和位置[bottom,top,width,height]
plt.axes([0.025, 0.025, 0.95, 0.95])
# alpha为透明度
plt.plot(X, Y + 1, color="blue", alpha=1.0)
# fill_between()方法为填充颜色(x,y1,y2,bool...)
plt.fill_between(X, 1, Y + 1, color="blue", alpha=0.25)
plt.plot(X, Y - 1, color="blue", alpha=1.0)
plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color="blue", alpha=0.25)
plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color="red", alpha=0.25)
# xticks()方法为设置横坐标的标记内容，这里空着就是没有标记
plt.xlim(-np.pi, np.pi), plt.xticks([])
plt.ylim(-2.5, 2.5), plt.yticks([])

plt.show()
