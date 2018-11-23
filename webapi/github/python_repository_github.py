#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
调用Web API并处理结果，找出GitHub上星级最高的Python项目
并进行数据可视化，改进Pygal图表
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
print('Number of items:', len(repo_dicts))
# 仓库名和制图数据集合
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': int(float(repo_dict['stargazers_count'])),
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],    # 在图表中添加可单击的链接
    }
    plot_dicts.append(plot_dict)
# 数据可视化
my_style = LS('#336699', base_style=LCS)    # 图形基色设置为深蓝色
my_config = pygal.Config()
my_config.x_label_rotation = 45    # 让标签绕x 轴旋转45度
my_config.show_legend = False    # 隐藏图例
my_config.title_font_size = 24    # 图表标题字体大小
my_config.label_font_size = 14    # 图表副标签字体大小
my_config.major_label_font_size = 18    # 图表主标签字体大小
my_config.truncate_label = 15    #  将较长的项目名缩短为15个字符（如果你将鼠标指向屏幕上被截短的项目名，将显示完整的项目名）
my_config.show_y_guides = False    # 隐藏图表中的水平线
my_config.width = 1000    # 自定义图表宽度
chart = pygal.Bar(my_config, style=my_style) 
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
# 渲染成SVG文件
chart.render_to_file('images/python_repository_github_3.svg')
