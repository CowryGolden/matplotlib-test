#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
同时投掷两个（相同个面的）骰子，并将出现的结果集合进行可视化显示
'''
import pygal
from die import Die

# 创建两个具有相同面（6个面）的骰子D6
die_1 = Die()
die_2 = Die()
# 掷多次骰子，并将结果存储在一个列表中
results = []
for roll_nun in range(1000000):
    result = die_1.roll() + die_2.roll()    # 计算每次总点数
    results.append(result)

# 分析结果
frequencies = []
x_labels = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    x_labels.append(value)
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
# 设置图表及坐标轴的标题，并给坐标轴加上标签
hist.title = "Results of rolling two D6 dices 1,000,000 times."
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# 将一系列值添加到图表中
hist.add('D6 + D6', frequencies)
# 将图表渲染为一个SVG文件(使用Web浏览器查看)
hist.render_to_file('images/dice2_visual.svg')
