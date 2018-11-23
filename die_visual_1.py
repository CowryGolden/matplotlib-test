#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
将投掷骰子出现的结果集合进行可视化显示
'''
import pygal
from die import Die

# 创建一个具有6个面的骰子D6
die = Die()
# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_nun in range(10000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
# 设置图表及坐标轴的标题，并给坐标轴加上标签
hist.title = "Results of rolling one D6 10000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# 将一系列值添加到图表中
hist.add('D6', frequencies)
# 将图表渲染为一个SVG文件(使用Web浏览器查看)
hist.render_to_file('images/die_visual.svg')
