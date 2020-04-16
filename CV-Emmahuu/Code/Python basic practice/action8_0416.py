# -*- coding:utf-8 -*-
#@Time: 2020/4/16
#@Author: EmmaHuu
#@File: action8
"""

 """
from datetime import datetime

# str = '2020/04/16 20:00:00'
# result = datetime.strptime(str, '%Y/%m/%d %H:%M:%S')
# str2 = '2020/04/17 20:00:00'
# result2 = datetime.strptime(str2, '%Y/%m/%d %H:%M:%S')
# print(result)

def check(enter_code, correct_code, current_date, expiration_date):
	condition1 = enter_code == correct_code
	condition2 =datetime.strptime(expiration_date, '%B %d, %Y') > datetime.strptime(current_date, '%B %d, %Y')
	return(condition1 & condition2)

print(check('123','123','September 5, 2014', 'October 1, 2014'))
print(check('123a','123','September 5, 2014', 'October 1, 2014'))
print(check('123','123','July 9, 2015', 'July 2, 2015'))
