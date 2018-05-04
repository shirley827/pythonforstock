import pandas as pd
import tushare as ts
import numpy as np
import datetime
import matplotlib
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

begin_time = '2016-01-01'
end_time = '2017-10-01'
code = "600036" #china merchant codes in datasets by changing it we can do research for other stocks
df = ts.get_hist_data(code, start=begin_time, end=end_time)
df = df.sort_index(0)
df_idx = df.index.values
del df["close"]
del df["high"]  #just using open value for predict so delete all the other value
del df["low"]
del df["volume"]
del df["price_change"]
del df["p_change"]
del df["ma5"]
del df["ma10"]
del df["ma20"]
del df["v_ma5"]
del df["v_ma10"]
del df["v_ma20"]
del df["turnover"]

tech_rets = df.pct_change() #pandas method for calculating the percentage changes
rets=tech_rets.dropna() #drop the NaN value

days = 365 #set one year as analyze and set all values needed for montecarlo analyze

dt = 1.0000000/days

mu = rets.mean() # calculate the mean value

sigma = rets.std() #calculate the standard deviation

np.random.normal(loc = 0,scale=1) #set a normal distribution


def stock_monte_carlo(start_price,days,mu,sigma): #monte_carlo monitor based on quantile regression
	price = np.zeros(days) #numpy method for create a all zero array
	price[0] = start_price
	shock = np.zeros(days)
	drift = np.zeros(days)
	for x in xrange(1,days):
		shock[x] = np.random.normal(loc=mu * dt,scale=sigma * np.sqrt(dt))
		drift[x] = mu * dt
		price[x] = price[x-1] + (price[x-1] *(drift[x] + shock[x]))
	return price

start_price = 17.91


for run in xrange(100):
	plt.plot(stock_monte_carlo(start_price,days,mu,sigma))


plt.xlabel("Days")
plt.ylabel("Price")

plt.title("Monte Carlo Analysis for China Merchant Bank")
plt.show()

