# -*- coding:utf-8 -*-
#@Time: 2020/4/19
#@Author: EmmaHuu
#@File: action11
"""

 """
import re
def numJewelsInStones(J:str, S:str):
	num = 0
	matches = [num + len(re.findall(i, S)) for i in J]
	return sum(matches)
print(numJewelsInStones('aA','aAAbbbb'))
print(numJewelsInStones('z','ZZ'))
