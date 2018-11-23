#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
读取世界人口JSON文件数据并进行分析，绘制人口地图。
Pygal中的地图制作工具要求数据为特定的格式：用国别码表示国家，以及用数字表示人口数量。
处理地理政治数据时，经常 需要用到几个标准化国别码集。
population_data.json中包含的是三个字母的国别码，但Pygal使用两个字母的国别码。
我们需要想办法根据国家名获取两个字母的国别码。 
'''
import json
import pygal_maps_world.maps

from country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'data/population_data.json'
with open(filename, 'r') as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))    # Python无法将字符串小数转为整数
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
# 根据人口数量将所有的国家分成三组：少于1000万的、介于1000万和10亿之间的以及超过10亿的
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
# 看看每个分作分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))        
# 创建世界地图实例
wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010: 0-10M', cc_pops_1)
wm.add('2010: 10M-1BN', cc_pops_2)
wm.add('2010: >1BN', cc_pops_3)
# 渲染地图成svg文件
wm.render_to_file('images/worldmap_world_population_2010.svg')
