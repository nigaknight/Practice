import matplotlib.pyplot as plt
# 绘制多轴图 分成几个子图 语法如下
# subplot(numRows,numCols,plotNum)
# 例子
plt.figure()
for ide, color in enumerate("rgbyck"):
    plt.subplot(320 + ide + 1, axisbg=color)
# 某个图占整个轴的例子
plt.figure()
plt.subplot(221)
plt.subplot(222)
plt.subplot(212)
plt.show()
