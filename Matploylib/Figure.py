import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
fig = plt.figure()
# 添加子图的两种方法
ax1 = fig.add_subplot(211)
ax2 = fig.add_axes([0.125, 0.1, 0.7, 0.3])
# 给每个图添加网格（axes为Figure对象中的子图）
for ax in fig.axes:
    ax.grid(True)
# 创建并添加两条直线的例子
fig2 = plt.figure()
line1 = Line2D(
    [0, 1], [0, 1], transform=fig2.transFigure, figure=fig2, color="r")
line2 = Line2D(
    [0, 1], [1, 0], transform=fig2.transFigure, figure=fig2, color="g")
fig2.lines.extend([line1, line2])
plt.show()
