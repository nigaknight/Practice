import matplotlib.pyplot as plt
# from matplotlib import rc
plt.figure()
X = [8, 9, 10, 11, 12, 13, 14]
Y = [493, 621, 691, 733, 797, 787, 661]
# rc('font', **{'family': 'sans-serif', 'sans-serif': ['Arial'], 'size': 12})
# params = {'text.usetex': False, 'mathtext.fontset': 'stixsans'}
# plt.rcParams.update(params)
# plt.tick_params()设置轴边标记的参数
plt.tick_params(
    width=2,
    labelsize=12,
    direction="in",
    axis="both",
    which="both",
    top="on",
    right="on",
    )
# plt.gca()获取子图，spines设置坐标轴的参数
ax = plt.gca()
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
plt.plot(
    X,
    Y,
    'bs',
    ms=4,
    mec='c',
    linestyle='-',
    label='Segmented Multiple Support Rods TWT')
plt.xlabel('Frequence(GHz)', fontsize=12)
plt.ylabel('Saturated Output Power(W)', fontsize=12)
plt.ylim(400, 1000)
plt.grid(True, which='major', lw=0.5, ls='-', color='0.8', zorder=1)
plt.legend(loc="upper right", frameon=True, framealpha=1, fontsize=12)
plt.show()
