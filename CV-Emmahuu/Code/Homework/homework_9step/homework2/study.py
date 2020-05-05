# -*- coding:utf-8 -*-
#@Time: 2020/5/3
#@Author: EmmaHuu
#@File: study
"""

 """
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5])
y = np.array([1,3,2,3,5])
plt.scatter(x,y)
# plt.grid()
def MAE_loss(y,y_hat):
    return np.mean(np.abs(y_hat - y))

y_hat = np.array([-2, -1, -1, 3, 5])
# print(MAE_loss(y, y_hat))
def linear(x, k , b):
    y = k * x - b

for k in np.arange(-2, 2, 0.1):
    for b in np.arange(-10, 10, 0.1):
        y_hat = [linear(xi, k, b) for xi in list(x)]
        current_loss = MAE_loss(y, y_hat)
        print(current_loss)