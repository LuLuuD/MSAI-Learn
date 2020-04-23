# -*- coding:utf-8 -*-
#@Time: 2020/4/23
#@Author: EmmaHuu
#@File: action14_0422
"""

 """
import random
from pprint import pprint
# result = []
# for n in range(5):
# 	templist = []
# 	for i in range(10):
# 		temp = random.randint(1, 100)
# 		templist.append(i)
# 	result.append(templist)
# pprint(result)
def guess(num:int, target):
	count = 1
	while num != target:
		count += 1
		if num > target:
			num = int(input('太大了，请重新输入：'))
		elif num < target:
			num = int(input('太小了，请重新输入：'))
		# guess(num, target)
	pprint('恭喜你，猜中了！共猜了{}次'.format(count))

target = random.randint(1, 100)
pprint('target is {}'.format(target))
input_num = int(input('请输入一个数字：'))
guess(input_num, target)