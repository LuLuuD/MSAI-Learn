# -*- coding:utf-8 -*-
#@Time: 2020/4/15
#@Author: EmmaHuu
#@File: action7_0415
"""

 """
def maxProfit(prices, max_profit = 0) -> int:
	if len(prices) == 0: return 0
	minprice = prices[0]
	for price in prices:
		if price < minprice:
			minprice = price
		if price - minprice > max_profit:
			max_profit = price - minprice
	return max_profit

print(maxProfit([]))
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2]))
print(maxProfit([7,6,4,3,1]))


