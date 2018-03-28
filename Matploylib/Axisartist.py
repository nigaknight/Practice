# Imports
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as AA

# Creat a new figure of size 10x6 points ,using 100 pots per inch
fig = plt.figure(figsize=(10, 6), dpi=80)
# Creat a new subplot from a grid of 1x1
# 使用Axes来创建axisartist图像
ax = AA.Axes(fig, [0.1, 0.1, 0.8, 0.8])
fig.add_axes(ax)
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
ax.axis['bottom'].set_axisline_style('->', size=1.5)


X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Plot cosine using blue color with a continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle='-', label='cosine')
# Plot sine using orange color with a continuous line of width 1 (pixels)
plt.plot(X, S, color="red", linewidth=2.5, linestyle='-', label='sine')
# Set x limits
plt.xlim(X.min() * 1.1, X.max() * 1.1)
# Set x ticks
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# Set y limits
plt.ylim(C.min() * 1.1, C.max() * 1.1)
# Set y ticks
plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color="blue", linestyle='--', linewidth=1.5)
# scatter() 标记点
plt.scatter([t], [np.cos(t)], 50, color="blue")
plt.plot([t, t], [0, np.sin(t)], color="red", linewidth=1.5, linestyle='--')
plt.scatter([t], [np.sin(t)], 50, color="red")
plt.annotate(
    r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
    xy=(t, np.sin(t)),
    xycoords='data',
    xytext=(+10, +30),
    textcoords='offset points',
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle='arc3,rad=0.2'))
plt.annotate(
    r'$\cos(\frac{2\pi}{3})=\frac{1}{2}$',
    xy=(t, np.cos(t)),
    xytext=(-90, -50),
    textcoords='offset points',
    fontsize=16,
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2')
)
# Save figure using 72 dots per inch
# savefig("../figures/exercice_2.png",dpi=72)
# Show result on screen
plt.legend(loc='upper left', frameon=False)
plt.show()
