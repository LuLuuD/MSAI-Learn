# -*- coding:utf-8 -*-
#@Time: 2020/4/28
#@Author: EmmaHuu
#@File: action20_0428
"""

 """
def findSubString(s :str, words: list) -> list:
	pattern = []
	def backtrace(node, L):
		if not L:
			pattern.append(node)
		for i in range(len(L)):
			backtrace(node + L[i], L[:i] + L[i+1:])
	backtrace('', words)
	result =[s.find(i) for i in pattern if i in s]
	return sorted(result)
print(findSubString('barfoothefoobarman',['foo','bar']))
print(findSubString('wordgoodgoodgoodbestword',['word','good','best','word']))
print(findSubString('wordgoodgoodgoodbestword',['good','best','word']))