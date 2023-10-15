import pandas as pd
import numpy as np
import os

path = 'D:\\codefile\\pycharm\\1\\filefolder'
file_input_name = []
for file_name in os.listdir(path):
    file_input_name.append(file_name)
for i in file_input_name:
    file_input = pd.read_excel(file_input_name)
    data_time = file_input.iloc[:200,0]
    data_value = file_input.iloc[:200,6]
    
    init_str = data_time[0]
    init_str1 = init_str.split(':')[2].split('.')[0]
    init_str2 = init_str.split('.')[1]
    
    
    data_time_re = []
    for i in range(len(data_time)):
        str = data_time[i]
        str1 = str.split(':')[2].split('.')[0]
        str2 = str.split('.')[1]
        return_str = 1000*(int(str1)-int(init_str1)) + (int(str2)-int(init_str2))
        #返回return_str和data_value
        data_time_re.append(return_str)
    
    date_value_abs = np.abs(data_value)
    date_re = pd.DataFrame({
        '时间':data_time_re,
        '值':date_value_abs
    })
    
    file_output_name = 're'+file_input_name
    date_re.to_excel(file_output_name,index=False)
    
    