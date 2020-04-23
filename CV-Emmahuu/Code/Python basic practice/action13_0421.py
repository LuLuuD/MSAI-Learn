# -*- coding:utf-8 -*-
#@Time: 2020/4/21
#@Author: EmmaHuu
#@File: action13_0421
"""

 """
# def searchInsert2(nums:list, target:int, result = 0) -> int:
# 	def splitNum(nums, target, middle):
# 		global result
# 		if target <= nums[middle] and target >= nums[middle - 1]:
# 			result += middle
# 		splitNum(nums[middle - comp::flag][::flag], target, middle)
# 	middle = len(nums) // 2
# 	comp = target < nums[middle]
# 	if len(nums) == 0: return 0
# 	if len(nums) == 1: return len(nums) - comp
# 	else:
# 		flag = 1 if target > nums[middle] else -1
# 		splitNum(nums, target, middle)
# 	return result

def searchInsert(nums:list, target:int) -> int:
	if target in nums: return nums.index(target)
	left, right = 0, len(nums) - 1
	while  left <= right:
		pivot = left + (right - left) // 2
		if target > nums[pivot]:
			left = pivot + 1
		else:
			right = pivot - 1
	return left




print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))