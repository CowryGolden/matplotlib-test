#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
将国家名称处理为两个字母的国别码，方便Pygal使用。
Pygal使用的国别码存储在模块i18n（internationalization的缩写）中。
字典COUNTRIES包含的键和值分别为两个字母的国别码和国家名。
'''
from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])