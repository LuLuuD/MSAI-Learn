# -*- coding:utf-8 -*-
#@Time: 2020/4/18
#@Author: EmmaHuu
#@File: action10_0418
"""

 """
def sort_by_name(arr):
	num_to_19 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen',
	           'Seventeen','Eighteen','Nineteen']
	num_to_90 = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
	unit = [' ', ' ', ' Hundred And ',' Thousand And ', ' Million And ',' Billion And ']
	new_arr = []
	def eng_name(n, result, time):
		def double(n):
			if n // 10 > 1:
				double_nam = num_to_90[n // 10 -2] + unit[1] + num_to_19[n % 10]
			else:
				double_nam = num_to_19[n]
			return double_nam
		length = len(str(n))
		if length == 3:
			result += num_to_19[n // 100] + unit[2] + double(n % 100)
		else:
			result += double(n)
		if time > 0: result += unit[2 + time]
		return result
	for num in arr:
		if len(str(num))//3 == 0:
			new_arr.append(''.join(eng_name(num,'', 0)))
		else:
			name_list = [eng_name((num//10**(3*i) % 10**3), '', i) for i in range(len(str(num))//3 -1 , -1, -1)]
			new_arr.append(''.join(name_list))
	order = arr.sort(key = new_arr)
	return order
print(sort_by_name([8, 8, 9, 9, 10, 10]))
print(sort_by_name([1, 2, 3, 4]))
print(sort_by_name([9, 99, 999]))


