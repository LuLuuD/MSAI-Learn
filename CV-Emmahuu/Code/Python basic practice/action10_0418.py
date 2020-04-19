# -*- coding:utf-8 -*-
#@Time: 2020/4/18
#@Author: EmmaHuu
#@File: action10_0418
"""

 """
import numpy as np
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
			# new_arr[num] = ''.join(eng_name(num,'', 0))
		else:
			name_list = [eng_name((num//10**(3*i) % 10**3), '', i) for i in range(len(str(num))//3 -1 , -1, -1)]
			new_arr.append(''.join(name_list))
			# new_arr[num] = ''.join(name_list)
	order = arr.sort(key = new_arr)
	return order
print(sort_by_name([8, 8, 9, 9, 10, 10]))
print(sort_by_name([1, 2, 3, 4]))
print(sort_by_name([9, 99, 999]))





# def sort_by_name2(arr):
# 	num_to_19 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen',
# 	           'Seventeen','Eighteen','Nineteen']
# 	num_to_90 = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
# 	unit = ['Billion','Million', 'Thousand']
# 	def three_num(num):
# 		H = num_to_19[num // 100] + ' Hundred'
# 		T = num_to_90[num % 100//10 - 2] if num % 100//10 > 1 else ''
# 		S = num_to_19[num % 10]  if num % 100 // 10 > 1 else num_to_19[num % 20]
# 		result = H +' and ' + T + ' ' + S if num // 100 else T + ' ' + S
# 		return result
# 		# for i in num:
# 		# 	if len(i) < 4:
# 		# 		H = num_to_19[i//100] + 'Hundred'
# 		# 		T = num_to_90[i%100-1%10]
# 		# 		S = num_to_19[i%100]
# 		# 		result = H + T + S if i//100 else T + S
# 		# 		return result
# 	result = []
# 	number = ''
# 	for i in arr:
# 		if len(str(i)) < 4:
# 			number = three_num(i)
# 		else:
# 			for time in range(len(str(i))//3):
# 				# number += three_num(i//10**(3*(2-time))) +' ' +  unit[time] + ' and ' + three_num(i//10**(3*(2-time) -4))
# 				number += three_num(i//10**(3*(2-time))) +' ' +  unit[time]
# 		result.append(number)
# 	print(1)
# 	# def strin(x, y, z):
# 	# 	if x < 10:
# 	# 		num.append(x)
# 	# 	num.append(strin(x%10, y + x%100 - x%10,z + x//100))
# 	# [strin(i, 0, 0) for i in arr]
# 	# 	return num
# 	# number = [strin(i) for i in arr]
# 	# def below100(num):
# 	# 	for i in num:
# 	# 		if i//10 <= 1:
# 	# 			number = num_to_19[i]
# 	# 		if len(i) < 3:
# 	# 			number = num_to_90[i%100] if i//10 > 1 else num_to_19[i]
# 	# 		else:
# 	# 			number =num_to_19[i//100] + 'Hundred' +
#
# 	# def sort(string:str):
# 	# 	circle = string
# 	# if len(number) < 3:
# 	# 	result = number


# print(sort_by_name([8,8,9,9,10,10]))
