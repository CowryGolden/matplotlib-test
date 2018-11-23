#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
读取世界人口JSON文件数据并进行分析，绘制人口地图。
使用Pygal的Worldmap制作各国人口数据的世界地图；
为练习在地图上呈现数字数据，我们来创建一幅显示三个北美国家人口数量的地图。
'''
import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'Populations of Countries in North America'
# Pygal根据这些数字自动给不同国家着以深浅不一的颜色（人口最少的国家颜色最浅，人口最多的国家颜色最深）
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('images/worldmap_na_populations.svg')
