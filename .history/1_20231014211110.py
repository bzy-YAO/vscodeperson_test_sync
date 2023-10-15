import pandas as pd
import numpy as np


file_input_name = '1.xlsx'
file_input = pd.read_excel(file_input_name)
data_time = file_input.iloc[:,0]
data_value = file_input.iloc[:,6]

# 15:27:27.280 正则匹配：后面的数据
str = data_time[0]
str1 = str.split(':')[2].split('.')[0]
str2 = str..split('.')[1]

# data_time_re = []
# for i in length(data_time):

#     print(data_time[i])
#     print(data_value[i])
