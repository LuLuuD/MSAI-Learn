# -----------------------------------（start）-----------------------------------
"""
Action1: 完成A+B Problem
    （练习平台：https://zoj.pintia.cn/problem-sets/91827364500/problems/91827364500）
"""

## Answer1：
while True:
    try:
        line = input()
        a = line.split()
        print int(a[0]) + int(a[1])
    except:
        break



# -------------------------------------------------------------------------------- 
"""
Action2：求和
    求2+4+6+8+...+100的求和，用Python该如何写？
"""
## Answer2：

# (待补)



# --------------------------------------------------------------------------------
"""
Action3:  统计全班的成绩
    班里有5名同学，现在需要你用numpy来统计下这些人在语文、英语、数学中的平均成绩、最小成绩、
最大成绩、方差、标准差。然后把这些人的总成绩排序，得出名次进行成绩输出。
"""

## Answer3：
# 将学生成绩生成narray
students = np.array([[68, 65, 30],
                     [95, 76, 98],
                     [98, 86, 88],
                     [90, 88, 77],
                     [80, 90, 90]])

# 利用numpy统计函数计算平均值、最小值、最大值、方差、标准差
final = np.array([np.mean(students, 0),
                  np.min(students, 0),
                  np.max(students, 0),
                  np.var(students, 0),
                  np.std(students, 0)]).T

subject_cols = ['语文', '数学', '英语']
name_cols = ['张飞', '关羽', '刘备', '典韦', '许褚']

# 打印输出
for i, sub in enumerate(subject_cols):
    print("{0}平均成绩: {1:.2f}".format(sub, final[i, 0]))
    print("{0}最低分: {1:.0f}".format(sub, final[i, 1]))
    print("{0}最高分: {1:.0f}".format(sub, final[i, 2]))
    print("{0}成绩方差: {1:.2f}".format(sub, final[i, 3]))
    print("{0}成绩标准差: {1:.2f}\n".format(sub, final[i, 4]))

score_total = np.sum(students, 1)               # 计算总成绩
score_rank_index = np.argsort(-score_total)     # 计算总成绩（高分————>低分）对应的索引

# 打印输出全班排名
for i, rk in enumerate(score_rank_index):
    print("第{2}名:{0}，总分:{1:.0f}".format(name_cols[rk], score_total[rk], i+1))

# -----------------------------------（end）---------------------------------------- 
