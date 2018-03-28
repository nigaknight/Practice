# Imports
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist.axislines as SubplotZero

# Creat a new figure of size 10x6 points ,using 100 pots per inch
plt.figure(figsize=(10, 6), dpi=80)
# Creat a new subplot from a grid of 1x1
plt.subplot(111)

X = np.linspace(-1, 1, 256, endpoint=True)
C, S= 2*X+1, 2*X-1

# Plot cosine using blue color with a continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle='-')
# Plot sine using orange color with a continuous line of width 1 (pixels)
plt.plot(X, S, color="red", linewidth=2.5, linestyle='-')
# Set x limits
plt.xlim(X.min() * 1, X.max() * 1)
# Set x ticks
# Set y limits
plt.ylim(C.min() * 1.1, C.max() * 1.1)
# Set y ticks
plt.yticks([])
plt.xticks([])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
plt.fill_between(X, -100, 0, X>0, color="blue", alpha=0.25)
X2 = np.linspace(0, 0.5, 256, endpoint=True)
# fill_between函数第一个参数是自变量，第二和第三个参数是关于第一个参数的函数
plt.fill_between(X2, 2*X2-1, 0, X2>0, color="blue", alpha=0.5)
# scatter() 标记点
plt.annotate(
    r'$C\beta_2<0$',
    xy=(0.75, 0.5),
    xycoords='data',
    xytext=(+10, +70),
    textcoords='offset points',
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle='arc3,rad=0.2'))
plt.annotate(
    r'$C\beta_2>0$',
    xy=(0.75, 2.5),
    xytext=(-90, -70),
    textcoords='offset points',
    fontsize=16,
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2')
)
# Save figure using 72 dots per inch
# savefig("../figures/exercice_2.png",dpi=72)
# Show result on screen
plt.show()
