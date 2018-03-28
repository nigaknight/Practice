import matplotlib.pyplot as plt
# 以下为matplotlib中文显示的解决方案
#coding:utf-8
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'
# from matplotlib import rc
plt.figure()
X = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
Y = [493, 621, 691, 733, 797, 787, 661, 631, 531, 562 ,513]
Z = [511, 609, 561, 464, 516, 514, 521, 521, 535, 492, 418]
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
    label=u'六夹持杆行波管')
plt.plot(
    X,
    Z,
    color='r',
    marker='o',
    linestyle='--',
    ms=4,
    mec='c',
    label=u'三夹持杆行波管')
plt.xlabel(u'频率(GHz)', fontsize=12)
plt.ylabel(u'饱和输出功率(W)', fontsize=12)
plt.ylim(400, 1000)
plt.grid(True, which='major', lw=0.5, ls='-', color='0.8', zorder=1)
plt.legend(loc="upper right", frameon=True, framealpha=1, fontsize=12)
plt.show()
