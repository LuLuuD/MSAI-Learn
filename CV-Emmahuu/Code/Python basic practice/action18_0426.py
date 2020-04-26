# -*- coding:utf-8 -*-
#@Time: 2020/4/26
#@Author: EmmaHuu
#@File: action18_0426
"""

 """
# import hashlib
# hashPoints = [hashlib.md5(i.encode('utf-8')).hexdigest() for i in timePoints]
def findMindDifference(timePoints: list) -> int:
	hashPoints = sorted(list(map(hashTrans,timePoints)))
	result = []
	for i in range(len(hashPoints) * 2 - 1):
		diff = hashPoints[(i + 1) % len(hashPoints)] - hashPoints[i % len(hashPoints)]
		result.append(diff + (abs(diff) > 720) * 1440)
	return min(result)

def hashTrans(timePoint) -> int:
	return int(timePoint[ : 2]) % 24 * 60 + int(timePoint[3 : ])

print(findMindDifference(["23:59", "00:00"]))
print(findMindDifference(["21:59", "00:30", "00:05", "20:55"]))
print(findMindDifference(["23:59", "00:30", "00:05", "20:55"]))