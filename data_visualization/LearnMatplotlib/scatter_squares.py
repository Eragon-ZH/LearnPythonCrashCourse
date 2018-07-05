import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x*x for x in x_values]

# x, y, (默认蓝点黑色轮廓), c点的颜色, edgecolor轮廓颜色, s点的大小
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors="none", s=50)
# 可以设置颜色映射 https://matplotlib.org/tutorials/index.html#tutorials-colors
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors="none", s=50)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标尺的大小
plt.tick_params(axis='both', which="major", labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 自动保存图表
# plt.savefig("squares_plot.png", bbox_inches="tight")

plt.show()
