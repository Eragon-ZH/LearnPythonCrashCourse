import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename = "sitka_weather_2014.csv"
filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 打印文件头， 显示各位置元素的意义
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # 看出每行第一个元素是日期，第二个元素是最高气温，第四个元素是最低气温
    # 获取日期、最高气温、最低气温
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # print(dates, highs)
# 绘制图形
fig = plt.figure(figsize=(15,10))
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
# 设置图形格式
# plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel("", fontsize=16)
# 让x轴日期倾斜
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which="major", labelsize=16)

plt.show()
