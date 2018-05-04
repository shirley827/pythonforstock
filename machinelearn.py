import pandas as pd
import tushare as ts
import sklearn as skl #using sklearn as a machinelearn tool
import numpy as np
import datetime
from sklearn import datasets,linear_model 

from sklearn.model_selection import train_test_split,cross_val_score #set the train data and test data random and doing crossvalidation for datas


date_end_str = '2018-01-03'
code = "600036"  #china merchant codes in datasets by changing it we can do research for other stocks

date_end = datetime.datetime.strptime(date_end_str, "%Y-%m-%d") #covert char to dates
date_start = (date_end + datetime.timedelta(days=-300)).strftime("%Y-%m-%d") #set the training dates as one year
date_end = date_end.strftime("%Y-%m-%d") #covert dates to char


stock_X = ts.get_hist_data(code, start=date_start, end=date_end)
stock_X = stock_X.sort_index(0)  #using data as index
stock_y = pd.Series(stock_X["close"].values) #create a NumPy ndarray

stock_X_test = stock_X.iloc[len(stock_X)-1] #search on the index by the length minus 1 and using the last data to 

stock_X = stock_X.drop(stock_X.index[len(stock_X)-1]) 
stock_y = stock_y.drop(stock_y.index[0]) 

del stock_X["close"]
del stock_X_test["close"]


stock_y_test = stock_y.iloc[len(stock_y)-1]

print(stock_X.tail(5))
print("###########################")
print(stock_y.tail(5)) 


print("###########################")
print(len(stock_X),",",len(stock_y))

print("###########################")
print(stock_X_test.values,stock_y_test)

model = linear_model.LinearRegression() #using LinearRegression model for machine learn
model.fit(stock_X.values,stock_y)
print("############## test & target #############")
print(model.predict([stock_X_test.values]))
print(stock_y_test)

print("############## coef_ & intercept_ #############")
print(model.coef_) 
print(model.intercept_) 
print("score:", model.score(stock_X.values,stock_y)) 