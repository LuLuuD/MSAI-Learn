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
	# pattern = re.compile('(?:rs\":\"([0-9\s]+).*?\"n\":\"(.*?)\")|(?:ln\":\"(.*?)\".*?lo\":\"(.*?)\")')
	lines_list = pattern.findall(str(text))
	lines_info = {}
	
	# 所有站点信息的dict：key：站点名称；value：站点坐标(x,y)
	stations_info = {}
	stations_list = []
	
	for i in range(len(lines_list)):
		# 你可能需要思考的几个问题，获取「地铁线路名称，站点信息list，站名，坐标(x,y)，数据加入站点的信息dict，将数据加入地铁线路dict」
		if lines_list[i][-1] == '':
			stations_info[lines_list[i][1]] = tuple(map(int, lines_list[i][0].split(' ')))
			stations_list.append(lines_list[i][1])
		else:
			lines_info[lines_list[i][2] + lines_list[i][3]] = stations_list
			stations_list = []
	print(lines_info)
	