# -*- coding:utf-8 -*-
#@Time: 2020/4/25
#@Author: EmmaHuu
#@File: action17
"""

 """
from collections import Counter

def removeDuplicates(elem: list):
	elem.reverse()
	for i in elem:
		while Counter(elem)[i] > 2:
			elem.remove(i)
	elem.reverse()
	return(elem)
print(removeDuplicates([1,1,1,2,2,3]))
print(removeDuplicates([1,2,2,3,5,2,4,5,3,2,1,5]))
print(removeDuplicates([3,2,2,1]))