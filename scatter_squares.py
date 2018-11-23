#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
绘制自然数平方数列的简单散点图
'''
import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# plt.scatter(x_values, y_values, s=40)    # s表示绘制点的尺寸
# plt.scatter(x_values, y_values, edgecolor='none', s=40)    # s表示绘制点的尺寸，散点默认为蓝色点和黑色轮廓；但绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，使用属性：edgecolor='none'
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)    # c表示数据点的颜色
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)    # c可以用RGB表示颜色，(红,绿,蓝)三个分量使用元组表示，其中包含三个0~1之间的小数【值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅】；(0, 0, 0.8)为淡蓝色表示
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)    # 使用颜色映射，从开始颜色渐变到结束颜色，从而突出数据规律；如：数值小颜色浅，数值大颜色深
# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])
# 保存图表
plt.savefig('images/squares_plot.png', bbox_inches='tight')
# 显示图形
plt.show()