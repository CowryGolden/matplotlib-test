#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
读取天气数据CSV文件(数据无错误)，解析其中的最高和最低温度
'''
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取日期和最高气温
# filename = 'data/sitka_weather_07-2014.csv'
filename = 'data/sitka_weather_2014.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)    # 读取第一行数据，文件头信息
    
    dates, highs, lows = [], [], []    # 日期、最高气温、最低气温集合
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)
    for row in reader:    # 从文件中获取最高气温
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
    # print(highs)
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')    # 绘制最高气温折线
plt.plot(dates, lows, c='blue')    # 绘制最低气温折线
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)    # facecolor-指定填充区域的颜色；alpha-位透明度（0-完全透明；1-完全不透明）
# 设置图形的格式
# plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()    # 自动格式化x轴的日期标签，以免它们重叠
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
# 显示图形
plt.show()