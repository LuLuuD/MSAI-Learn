# -*- coding:utf-8 -*-
#@Time: 2020/4/26
#@Author: EmmaHuu
#@File: tst
"""

 """
class Solution:
    def findMindDifference(self, timePoints: list)-> int:
        hashPoints = sorted(list(map(self.hashTrans,timePoints)))
        result = []
        for i in range(len(hashPoints) * 2 - 1):
            diff = hashPoints[(i + 1) % len(hashPoints)] - hashPoints[i % len(hashPoints)]
            result.append(diff + (abs(diff) > 720) * 1440)
        return min(result)

    def hashTrans(self, timePoint) -> int:
        return int(timePoint[ : 2]) % 24 * 60 + int(timePoint[3 : ])
