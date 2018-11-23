#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
将国家名称处理为两个字母的国别码，方便Pygal使用。
Pygal使用的国别码存储在模块i18n（internationalization的缩写）中。
字典COUNTRIES包含的键和值分别为两个字母的国别码和国家名。
'''
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """ 根据指定的国家名称，返回Pygal使用的两个字母的国别码 """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定的国家，就返回None
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))


