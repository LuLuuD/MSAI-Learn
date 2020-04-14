# -*- coding:utf-8 -*-
#@Time: 2020/4/14
#@Author: EmmaHuu
#@File: action6_0414
"""

 """
import queue

class MovingAverage:
	def __init__(self, size: int):
		self.container = queue.Queue(size)
	def next(self, val: int) -> float:
		if self.container.full():
			self.container.get()
		self.container.put(val, block = True, timeout = 5)
		return sum(self.container.queue)/self.container.qsize()
		
m = MovingAverage(3)
print(m.next(1))
print(m.next(10))
print(m.next(5))
print(m.next(6))