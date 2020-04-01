import matplotlib.pyplot as plt
import pandas as pd
import datetime, os, warnings

warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #可以显示负号

# 设置起始时间
start = datetime.datetime(2020,1,1)
end = datetime.datetime(2020,3,31)
# print(start)

from pandas_datareader.data import DataReader
# 读取上证综指 及 A股指数数据
def load_data():
	if os.path.exists('000001.csv'):
		data_ss = pd.read_csv('000001.csv')
	else:
		# 上证综指
		data_ss = DataReader("000001.SS", "yahoo", start, end)
		data_ss.to_csv('000001.csv')

	if os.path.exists('000002.csv'):
		data_tlz = pd.read_csv('000002.csv')
	else:
		# A股指数
		data_tlz = DataReader("000002.SS", "yahoo", start, end)
		data_tlz.to_csv('000002.csv')

	return data_ss, data_tlz

data_ss, data_tlz = load_data()

# A股指数与上证综指
close_ss = data_ss["Close"]
close_a = data_tlz["Close"]

# 数据可视化
fig = plt.figure(figsize=[15, 7])
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.suptitle('数据比对', fontsize=20)
plt.subplot(121)
plt.plot(close_ss, label='上证综指收盘价')
plt.legend()
plt.subplot(122)
plt.plot(close_a, label='A股指数收盘价')
plt.legend()
plt.show()

# 将A股指数与上证综指进行数据合并
stock = pd.merge(data_ss, data_tlz, left_index = True, right_index = True)
stock = stock[["Close_x","Close_y"]]
stock.columns = ["上证综指","A股指数"]

# 统计每日收益率
daily_return = (stock.diff()/stock.shift(periods = 1)).dropna()
print(daily_return.head())
# 找出当天收益率大于10%的，应该是没有，因为涨停为10%
print(daily_return[daily_return["A股指数"] > 0.01])

# 每日收益率可视化
fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(15,6))
daily_return["上证综指"].plot(ax=ax[0])
ax[0].set_title("上证综指")
daily_return["A股指数"].plot(ax=ax[1])
ax[1].set_title("A股指数")
plt.show()


# 散点图
fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(12,6))
plt.scatter(daily_return["A股指数"],daily_return["上证综指"])
plt.title("每日收益率散点图 from A股指数 & 上证综指")
plt.show()

# 回归分析
import statsmodels.api as sm
# 加入截距项
daily_return["intercept"]=1.0
model = sm.OLS(daily_return["A股指数"],daily_return[["上证综指","intercept"]])
results = model.fit()
print(results.summary())