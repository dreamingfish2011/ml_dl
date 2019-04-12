import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def cal_age(x):
    return 2019 - x


area = 'bj'
filename = "guazi_car_" + area + ".csv"
data = pd.read_csv(filename, header=0)
data.columns = ["city", "title", "brand", "brand_series", "version", "year", "distance",
                "disaplacement", "tl_number", "price", "guiding_price", "service", "is_strict"]

print(data.describe())
print(data.isnull().sum())

data['distance'] = data['distance'].astype('float')
data['tl_number'] = data['tl_number'].astype('float')
data['year'] = data['year'].astype('int32')
data['age'] = data['year'].apply(cal_age)
data['price'] = data['price'].astype('float')
data['guiding_price'] = data['guiding_price'].astype('float')
data['remain_ratio'] = data['price'] / data['guiding_price']
bins = [0, 3, 6, 9, 12, 20]
data['dis_area'] = pd.cut(data.distance, bins, right=True)
bins = [0, 3, 6, 9, 12, 15, 25]
data['price_area'] = pd.cut(data.price, bins, right=True)
bins = [0, 3, 6, 9, 12, 15, 25, 100]
data['guiding_price_area'] = pd.cut(data.guiding_price, bins, right=True)
##行驶里程计数
# y = data.groupby(['dis_area'])['dis_area'].count()
# y.plot(rot=30)
##车龄和平均行驶里程关系
# y = data.groupby(['age'])['distance'].mean()
# x = np.arange(0, 12, 1)
# plt.bar(x,y)
##车龄和数量关系
# y = data.groupby(['age'])['distance'].count()
# x = np.arange(0, 12, 1)
# plt.bar(x,y)
##车龄和残值率关系
# y = data.groupby(['age'])['remain_ratio'].mean()
# x = np.arange(0, 12, 1)
# plt.bar(x, y)
##二手车价格关系
# y = data['price_area'].value_counts()
# y.plot.bar(rot=10)
##二手车价格关系
# y = data['guiding_price_area'].value_counts()
# y.plot.bar(rot=10)
# 年份原价和售卖价格
# y_price = data.groupby(['year'])['price'].mean()
# y_guiding_price = data.groupby(['year'])['guiding_price'].mean()
# x = np.arange(2008, 2020, 1)
# plt.plot(x, y_price, 'r--', x, y_guiding_price, 'g^')
# plt.plot(y.index, y)
y_price = data.groupby(['price_area'])['age'].mean()
y_guiding_price = data.groupby(['guiding_price_area'])['age'].mean()
plt.show()
