# -*- coding:utf-8 -*-
#@Time: 2020/4/23
#@Author: EmmaHuu
#@File: action15_0423
"""

 """
import heapq
import pandas as pd
# nums = [12,8,10,5,36,4,32]
# heapq.heapify(nums)
# print(nums)
# a = stock['shares'].values.tolist()
# heapq.heapify(a)
# print(a)

stock = pd.DataFrame([[150, 165.51], [50, 174.79], [320, 19.63], [100, 121.15], [75, 1210.41]],columns=['shares', 'price'], index = ['MSFT', 'FB', 'YHOO', 'IBM', 'GOOG'])
print('价格最高的两只股票：{}'.format([stock['price'].index.values[stock['price'] == i][0] for i in heapq.nlargest(2, stock['price'])]))
print('买入shares最多的两只股票：{}'.format([stock['shares'].index.values[stock['shares'] == i][0] for i in heapq.nlargest(2, stock['shares'])]))
