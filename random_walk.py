#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
定义随机漫步类
将创建一个名为RandomWalk 的类，它随机地选择前进方向。
这个类需要三个属性，其中一个是存储随机漫步次数的变量，其他两个是列表，分别存储随机漫步经过的每个点的 x 和 y 坐标。 
'''
from random import choice

class RandomWalk():
    """ 一个生成随机漫步数据的类 """

    def __init__(self, num_points=5000):
        """ 初始化随机漫步的属性 """
        self.num_points = num_points
        # 所有随机漫步都始于(0, 0)，定义两个存储x和y值的列表
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ 计算随机漫步包含的所有点 """
        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_step = self.get_x_step()
            y_step = self.get_y_step()
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step    # x_values[-1]表示x_values列表中的最后一个值
            next_y = self.y_values[-1] + y_step    # y_values[-1]表示y_values列表中的最后一个值
            # 将获取到的下一个点的x和y值追加到x_values和y_values列表末尾
            self.x_values.append(next_x)
            self.y_values.append(next_y)
    
    def get_x_step(self):
        """ 获取x轴方向移动的距离 """
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        return x_direction * x_distance

    def get_y_step(self):
        """ 获取y轴方向移动的距离 """
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        return y_direction * y_distance
