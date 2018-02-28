import matplotlib
import os
import pylab
# 获得用户配置路径
print("the user config is ", matplotlib.get_configdir())
# 获得当前配置文件路径
print("the current config is ", matplotlib.matplotlib_fname())
# 获得当前文件路径
print(os.getcwd())
# rc_params返回一个配置字典
print("the return of rc_params are \n", matplotlib.rc_params())
# 使用matplotlib时会自动调用rc_params,并将返回的配置字典保存在rcparams中
print("the rcparams are \n", matplotlib.rcParams)
# 修改配置(绘制的线带有点标识符)
pylab.figure()
matplotlib.rcParams["lines.marker"] = 'o'
pylab.plot([1, 2, 3])
# 使用rc简便地修改配置
pylab.figure()
# 这里设置颜色失败，不知道是什么情况
matplotlib.rc("lines", color="red", marker="x", linewidth=2)
pylab.plot([1, 2, 3])
# 恢复缺省配置
pylab.figure()
matplotlib.rcdefaults()
pylab.plot([1, 2, 3])
pylab.legend()
pylab.show()
