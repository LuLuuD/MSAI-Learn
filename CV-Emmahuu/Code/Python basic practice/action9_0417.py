# -*- coding:utf-8 -*-
#@Time: 2020/4/17
#@Author: EmmaHuu
#@File: action9_0417
"""
path剔除路径
 """
# def permutations(string):
# 	res = set()
# 	def backtrack(S, path):
# 		if not S:
# 			res.add(path)
# 		for i in range(len(S)):#每个结点
# 			backtrack(S[:i] + S[i+1:], path + S[i])
# 	backtrack(string, '')
# 	return res

def permutations(string):
	res = set()
	def backtrack(node, S):
		if not S:
			res.add(node)
		for i in range(len(S)):
			backtrack(node + S[i], S[:i] + S[i+1:])
	backtrack('', string)
	return res

print(permutations('a'))
print(permutations('ab'))
print(permutations('aabb'))