import numpy as np

persontype = np.dtype({'names':['姓名', '语文', '数学', '英语'], 'formats':['S32','i', 'i', 'i']})
datas = np.array([('张飞'.encode('gbk'), 68, 65, 30), ('关羽'.encode('gbk'), 95, 76, 98), ('刘备'.encode('gbk'), 98, 86 , 88),
                  ('典韦'.encode('gbk'), 90, 88, 77), ('许褚'.encode('gbk'), 80, 90, 90)],dtype=persontype)

chinese = datas['语文']
math = datas['数学']
english = datas['英语']

print(np.mean(chinese))
print(np.mean(math))
print(np.mean(english))
print(np.min(chinese))
print(np.min(math))
print(np.min(english))
print(np.max(chinese))
print(np.max(math))
print(np.max(english))
print(np.var(chinese))
print(np.var(math))
print(np.var(english))
print(np.std(chinese))
print(np.std(math))
print(np.std(english))

arr = []
for row in range(len(datas)):
    sum = 0
    for col in range(len(datas[0])):
        if col != 0:
            sum += datas[row][col]
    arr.append(sum)

arr.sort()
print(arr)