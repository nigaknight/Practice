# -*- coding: utf-8 -*-
# 两个库matploylib.pyplot和numpy
import matplotlib.pyplot as plt
import numpy as np

# numpy为python的数值计算扩展，这里用到的是一个强大的n维数组对象
x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

# matplotlib为python的绘图库，pyplot为其字库
# figure(figsize=())->plot()->title(),xlable(),ylabel(),ylim()->legend()->show()
# 开始绘图，设置图像大小->绘制曲线->设定标题，x轴y轴标签，y轴取值范围等->显示图示->显示所有
plt.figure(figsize=(8, 4))
plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")
plt.title("Pyplot First Example")
plt.xlabel("Time(s)")
plt.ylabel("volt")
plt.ylim(-1.2, 1.2)
plt.legend()
plt.show()
