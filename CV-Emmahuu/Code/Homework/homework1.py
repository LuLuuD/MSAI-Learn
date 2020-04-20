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

	def get_neighbor_info(lines_info):
		
		# 把str2加入str1站点的邻接表中
		def add_neighbor_dict(info, str1, str2):
			# 请在这里写代码
			if str1 not in info.keys():
				info[str1] = []
			if str2 not in info.keys():
				info[str2] = []
			info[str1].append(str2)
			info[str1].append(str2)
		
		neighbor_info = {}
		for item in lines_info.items():
			for i in range(len(item[1]) - 1):
				add_neighbor_dict(neighbor_info, item[1][i], item[1][i + 1])
			if item[0][-1] == '1':
				add_neighbor_dict(neighbor_info, item[1][-1], item[1][0])
		return neighbor_info
	
	
	neighbor_info = get_neighbor_info(lines_info)
	
	
	def get_path_DFS_ALL(lines_info, neighbor_info, from_station, to_station):
		# 递归算法，本质上是深度优先
		# 遍历所有路径
		# 这种情况下，站点间的坐标距离难以转化为可靠的启发函数，所以只用简单的BFS算法
		# 检查输入站点名称
		res = get_next_station_DFS_ALL([{from_station}, -1, [from_station]], neighbor_info, to_station)
		return res[-1]
	
	
	def get_next_station_DFS_ALL(node, neighbor_info, to_station):
		res = []
		if node[1] != -1 and len(node[-1])>node[1]:
			return res
		if node[-1][-1] == to_station:
			node[1] = len(node[-1])
			return [node[-1].copy()]
		nextStations = neighbor_info[node[-1][-1]]
		return res
	
	
	res = get_path_DFS_ALL(lines_info, neighbor_info, '大兴机场', '航站楼')
	
	