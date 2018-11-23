#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
读取世界人口JSON文件数据并进行分析，绘制人口地图。
使用Pygal的Worldmap制作各国人口数据的世界地图；
这里我们创建一个突出北美、中美和南美的简单地图。
'''
import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('images/worldmap_americas_map.svg')