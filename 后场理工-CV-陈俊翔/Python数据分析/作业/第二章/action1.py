import random

host = '''
host = 寒暄 报数 询问 具体业务 结尾
报数 = 我是工号 数字 号 ,
数字 = 单个数字 | 数字 单个数字
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好
询问 = 请问你要 | 您需要
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？
'''

def getGrammarDict(gram, linesplit = "\n", gramsplit = "="):
    #定义字典
    result = {}

    for line in gram.split(linesplit):
        # 去掉首尾空格后，如果为空则退出
        if not line.strip():
            continue
        expr, statement = line.split(gramsplit)
        result[expr.strip()] = [i.split() for i in statement.split("|")]
    print(result)
    return result

def generate(gramdict, target, isEng = False):
    if target not in gramdict:
        return target
    find = random.choice(gramdict[target])
    # print(find)
    blank = ''
    # 如果是英文中间间隔为空格
    if isEng:
        blank = ' '
    return blank.join(generate(gramdict, t, isEng) for t in find)

gramdict = getGrammarDict(host)
print(generate(gramdict,"host"))