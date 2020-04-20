# -*- coding:utf-8 -*-
#@Time: 2020/4/20
#@Author: EmmaHuu
#@File: action12_0420
"""

 """
def longest_palindrome(string:str):
	length = []
	for i in string:
		if string[string.find(i):string.rfind(i) + 1] == string[string.find(i):string.rfind(i) + 1][::-1]:
			length.append(string[string.find(i):string.rfind(i) + 1])
	return max([len(i) for i in length])

print(longest_palindrome("a"))
print(longest_palindrome("aa"))
print(longest_palindrome("baa"))
print(longest_palindrome("aab"))
print(longest_palindrome("abcdefghba"))
print(longest_palindrome("baablkj12345432133d"))