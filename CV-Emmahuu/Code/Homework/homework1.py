# -*- coding:utf-8 -*-
# @Time: 2020/4/20
# @Author: EmmaHuu
# @File: homework1
"""

 """
import requests
import json
import re
import numpy as np
import pandas as pd
# requests.adapters.DEFAULT_RETRIES = 5
# headers = {
#     'Connection': 'close'
# }
# r  = requests.session()
# r.keep_alive = False
# r = requests.get('http://10.20.28.209:8090/mir/report/MIR/Wafer%20Sort/MetrologySkipReport.jsp?ticket=ST-636659-HDVBeLKv71p2LzGLb1jF')
# print(r.text)

# with open('subway.json', mode = 'r', encoding='utf-8') as f0:
# 	text = json.load(f0)
# 	df = pd.DataFrame(data = text['l'])
# 	print(text)

#text[l]中，ln是几号线；st里的rs是坐标，n是站点名
with open('subwaytext.txt', mode = 'r', encoding='utf-8') as f:
	text = f.readlines()[0]
	pattern = re.compile('(?:rs\":\"([\d\s]+).*?\"n\":\"(.*?)\")|(?:ln\":\"(.*?)\".*?lo\":\"(\d?)\")')
	# match = re.compile('(?:rs\":\"(\d\s\d+).*\"n\":\"(.*)\")|(()())')
	pattern = re.compile('(?:rs\":\"([0-9\s]+).*?\"n\":\"(.*?)\")|(?:ln\":\"(.*?)\".*?lo\":\"(.*?)\")')
	lines_list = pattern.findall(str(text))
	print(lines_list)