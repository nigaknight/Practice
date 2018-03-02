import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot([1, 2, 3])
# patch为figure对象的背景属性，可以对它进行修改，set_*
fig.patch.set_color("g")
plt.legend()
plt.show()
