#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
调用Web API并处理结果，找出GitHub上星级最高的Python项目
并进行数据可视化
'''
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)
# 将API响应存储在一个变量中
response_dict = r.json()
print('Total repositories:', response_dict['total_count'])
# 探索有关仓库的信息
repo_dicts = response_dict['items']
# 仓库名和星数集合
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
# 数据可视化
my_style = LS('#336699', base_style=LCS)    # 图形基色设置为深蓝色
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)    # x_label_rotation=45-代表让标签绕x 轴旋转45度；show_legend=False-代表隐藏图例
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('Stars', stars)
# 渲染成SVG文件
chart.render_to_file('images/python_repository_github_1.svg')
