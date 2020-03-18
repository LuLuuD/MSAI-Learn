#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
_date_ = '2020/3/17 14:45'
_author_ = 'Joe'

import numpy as np
import pandas as pd
name = ["张飞","关羽","刘备","典韦","许褚","均值","最大值","最小值","方差","标准差"]
chinsese = [68,95,98,90,80]
math = [65,76,86,88,90]
english = [30,98,88,77,90]
#计算总成绩
score = np.add(chinsese,math)
score = np.add(score,english)
score = np.append(score, values=[0,0,0,0,0], axis=0)
#计算各科均值、最大值。。。
chinsese = np.append(chinsese, [np.mean(chinsese),np.max(chinsese), np.min(chinsese), np.var(chinsese), np.std(chinsese)])
math = np.append(math, [np.mean(math),np.max(math), np.min(math), np.var(math), np.std(math)])
english = np.append(english, [np.mean(english),np.max(english), np.min(english), np.var(english), np.std(english)])
#建立表头
students = {'name':name,'chinese':chinsese,\
                 'math':math,'english':english,'score':score}
#建立数据表
df = pd.DataFrame(students)
#列排序
df = df[['name', 'chinese', 'math', 'english','score']]
#成绩降序
df = df.sort_values(by='score', ascending=False, axis=0)
df = df.round(2)
print(df)




