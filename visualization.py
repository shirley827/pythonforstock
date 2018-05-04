import pandas as pd  #python data anlyse lib
import tushare as ts
import datetime #python lib for deal with dates
import matplotlib
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
import matplotlib.pyplot as plt  #lib for drawing picture
import mpl_finance as mpl  #dataset for stock
import matplotlib.ticker as ticker  #lib for locating and formating
begin_time = '2017-07-01'
end_time = '2017-10-01'
code = "600036" #china merchant bank's code in the dataset
df = ts.get_hist_data(code, start=begin_time, end=end_time) #a list
df = df.sort_index(0) #use dates as index
df_idx = df.index.values
fig, ax = plt.subplots(figsize=(20, 10)) #set the picture size
mpl.candlestick2_ochl(ax = ax, 
                 opens=df["open"].values, closes=df["close"].values,
                 highs=df["high"].values, lows=df["low"].values, 
                 width=0.75, colorup='r', colordown='g', alpha=0.75)
ax.xaxis.set_major_locator(ticker.MaxNLocator(20)) # draw the candlestick picture by using mpl_finance lib and set locations

def mydate_formatter(x,pos):
    try:
        return df_idx[int(x)]
    except IndexError:
        return ''

ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate_formatter))
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
ax.grid(True) #show grids in the picture
plt.title("China Merchants Bank") #set titles
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()