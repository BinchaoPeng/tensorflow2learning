from sklearn import datasets
from pandas import DataFrame
import pandas as pd

x_data = datasets.load_iris().data
y_data = datasets.load_iris().target
print(x_data)
print(y_data)

# set a table header
x_data = DataFrame(x_data,
                   columns=['花萼长度', '花萼宽度', '花瓣长度', '花瓣宽度'])
# Set column name alignment
pd.set_option('display.unicode.east_asian_width', True)
print(x_data)

# add a new column
x_data['class'] = y_data
print(x_data)
