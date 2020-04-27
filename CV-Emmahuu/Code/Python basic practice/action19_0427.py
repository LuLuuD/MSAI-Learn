# -*- coding:utf-8 -*-
#@Time: 2020/4/27
#@Author: EmmaHuu
#@File: action19_0427
"""

 """
# a = 2
# b = '{:08b}'.format(a)
# print(b)
#
# print(2^3)

def hammingDistance(x: int, y: int) -> int:
	dis = x^y
	sum = 0
	while dis:
		sum += dis & 1
		dis = dis>>1
	return sum
print(hammingDistance(1,4))
print(hammingDistance(20,34))
print(hammingDistance(55,34))
print(hammingDistance(78,96))
print(hammingDistance(1278,196))
