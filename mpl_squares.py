#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
绘制自然数平方数列的简单折线图 
'''
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# 设置线条粗细
plt.plot(input_values, squares, linewidth=5)
# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
# 显示图形
plt.show()