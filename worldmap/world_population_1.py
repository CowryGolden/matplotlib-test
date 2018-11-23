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

from country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'data/population_data_update.json'
with open(filename, 'r') as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))    # Python无法将字符串小数转为整数
        print(country_name + ': ' + str(population))
        code = get_country_code(country_name)
        if code:
            print(code + ': ' + str(population))
        else:
            print('ERROR - ' + country_name)
