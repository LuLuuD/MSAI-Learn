# -*- coding:utf-8 -*-
#@Time: 2020/4/11
#@Author: EmmaHuu
#@File: action3
"""

 """
def duplicate_count(text):
	if text.isalnum():
		text_dic = {}
		count = 0
		for i in range(len(text)):
			if text[i] not in text[:i]:
				text_dic[text[i]] = 1
			else:
				text_dic[text[i]] += 1
		for m,n in text_dic.items():
			if n > 1:
				count += 1
		print('The result is {}'.format(count))
	else:
		print("Only numbers/letters are acceptable.")
		text = input("pls input numbers/letters only:")
		duplicate_count(text.lower())

text = input("pls input numbers/letters only:")
duplicate_count(text.lower())
