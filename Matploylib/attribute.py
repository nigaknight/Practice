import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 5, 0.1)
plt.figure(figsize=(8, 4))
# 设置属性的两种方法
# 方法一：对象的set_*()方法
line, = plt.plot(x, x * x)
line.set_antialiased(False)
# 方法二：pyplot的setp()方法
lines = plt.plot(x, np.sin(x), x, np.cos(x))
plt.setp(lines, color="red", linewidth=2.0)
# 获取属性的两种方法
# 方法一：对象的get_*()方法
print(line.get_linewidth())
# 方法二：pyplot的getp()方法
print(plt.getp(lines[0], "color"))
print(plt.getp(lines[1]))
plt.legend()
plt.show()
