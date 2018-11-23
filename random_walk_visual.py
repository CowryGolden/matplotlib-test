#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
绘制随机漫步（所有点）图，模拟多次随机漫步
为突出每次漫步的重要特征，并让分散注意力的元素不那么显眼。为此，我们确定要突出的元素，如漫步的起点、终点和经过的路径。
'''
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()
    # 设置绘图窗口尺寸
    plt.figure(dpi=128, figsize=(10, 6))
    # 使用颜色映射来指出漫步中各点的先后顺序，并删除每个点的黑色轮廓，让它们的颜色更明显
    # 由于这些点是按顺序绘制的，因此给参数c 指定的列表只需包含数字1~5000
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)    # 散点图
    # plt.plot(rw.x_values, rw.y_values, linewidth=1)    # 更换为折线图
    # 突出显示起点和终点
    plt.scatter(0, 0, c='green', edgecolors=None, s=100)    # 起点
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors=None, s=100)    # 终点
    # 隐藏坐标轴，以便关注随机漫步路径
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # 显示图形
    plt.show()
    # 根据用户输入判断是否进行下一次随机漫步
    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break