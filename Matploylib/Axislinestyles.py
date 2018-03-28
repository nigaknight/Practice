import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(1)
ax = AA.Axes(fig, [0.1, 0.1, 0.8, 0.8])
fig.add_axes(ax)
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
plt.show()