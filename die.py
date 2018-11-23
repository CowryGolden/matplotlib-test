#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
管理骰子的属性和方法
'''
from random import randint

class Die():
    """ 表示一个骰子的类 """

    def __init__(self, num_sides=6):
        """ 骰子默认为6个面 """
        self.num_sides = num_sides

    def roll(self):
        """ 返回一个位于1和骰子面数之间的随机整数，表示投掷骰子掷出的数字 """
        return randint(1, self.num_sides)
