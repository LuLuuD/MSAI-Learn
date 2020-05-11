# -*- coding:utf-8 -*-
#@Time: 
#@Author: EmmaHuu
#@File: price
"""

"""
from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = load_boston()
# pd.read_json(data)
print(data)
x_ = data['data']
y = data['target']
y = y.reshape(y.shape[0], 1)

#规范化
x_ = (x_ - np.mean(x_, axis = 0)) / np.std(x_, axis = 0)

#定义参数
n_features = x_.shape[1] #rows_样本数，cols_特征数
n_hidden = 10 #隐藏层数
w1 = np.random.randn(n_features, n_hidden)
b1 = np.zeros(n_hidden) # bias
w2 = np.random.randn(n_hidden, 1) #输出是从隐藏层到输出层，而输出层只有1层，所以是1维
b2 = np.zeros(1)

learning_rate = 1e-6

#激活函数
def Relu(x):
    result = np.where(x<0 , 0, x)
    return result

#线性函数
def Linear(x, w, b):
    y = x.dot(w) + b
    return y

#评估损失
def MSE_loss(y, y_hat):
    return np.mean(sum(np.square(y-y_hat)))

#前向传播
for t in range(5000):
    l1 = Linear(x_, w1, b1)
    s1 = Relu(l1)
    y_pred = Linear(s1, w2, b2)

    #计算损失函数
    loss = MSE_loss(y, y_pred)
    print(t, loss)

    #反向传播
    grad_y_pred = 2 * (y_pred - y) #求导
    grad_w2 = s1.T.dot(grad_y_pred)
    grad_temp_relu = grad_y_pred.dot(w2.T)
    grad_temp_relu[l1<0] = 0
    grad_w1 = x_.T.dot(grad_temp_relu)

    #权值更新
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2

print(' w1 = {}\n w2 = {}\n'.format(w1, w2))

