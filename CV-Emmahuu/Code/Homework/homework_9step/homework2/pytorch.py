# -*- coding:utf-8 -*-
#@Time: 
#@Author: EmmaHuu
#@File: pytorch
"""

"""

import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
import numpy as np
import torch

np.random.seed(33)
X,y = make_moons(200, noise = 0.2) #X是数据，y是标签
print(X)
print(y)
cm = plt.cm.get_cmap('RdYlBu')
plt.scatter(X[:,0], X[:, 1], c = y, cmap = cm)
plt.show()

X = torch.from_numpy(X).type(torch.FloatTensor)
y = torch.from_numpy(y).type(torch.LongTensor)
print(X)
print(y)
