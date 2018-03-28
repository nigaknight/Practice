import matplotlib.pyplot as plt

# quants: GDP
# labels: country name
labels = []
quants = []

# Read data
# 在 try 块中获取资源，然后在 finally 块中释放资源是一种常见的模式。因此，还有一个with 语句使得这一过程可以以一种干净的姿态得以完成。
with open('major_country_gdp.txt',
          'r') as f:
    # str.split()将字符串中的空格隔开的字符分开来为几个字符串
    for line in f:
        info = line.split()
        labels.append(info[0])
        quants.append(float(info[1]))

print(quants)
# make a square figure
plt.figure(1, figsize=(6, 6))


# For China, make the piece explode a bit
def explode(label, target='China'):
    if label == target:
        return 0.1
    else:
        return 0


# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个
# 新的 list 并返回。
expl = list(map(explode, labels))

# Colors used. Recycle if not enough.
colors = ["pink", "coral", "yellow", "orange"]

# Pie Plot
# autopct: format of "percent" string;
plt.pie(
    quants,
    explode=expl,
    colors=colors,
    labels=labels,
    # autopct表示每块所占的比例
    autopct='%1.1f%%',
    # 每个饼图切片的中心与文本的开始之间的距离比率
    pctdistance=0.8,
    shadow=True)
plt.title('Top 10 GDP Countries (2011)', bbox={'facecolor': '0.8', 'pad': 5})

plt.show()
