import pandas as pd
import numpy as np
import os

stop_steps = 201
path = './filefolder'
path_output = './output'
file_input_name = []

for file_name in os.listdir(path):
    file_input_name.append(file_name)

for file_input_name_num in range(len(file_input_name)):
    file_name_re = path + '\\' + file_input_name[file_input_name_num]
    file_output_name = file_input_name[file_input_name_num].split('.xlsx')[0] + '_re.xlsx'
    file_input = pd.read_excel(file_name_re)
    data_time = file_input.iloc[:stop_steps,0]
    data_value = file_input.iloc[:stop_steps,6]

    init_str = data_time[0]
    init_str1 = init_str.split(':')[2].split('.')[0]
    init_str2 = init_str.split('.')[1]


    data_time_re = []
    for i in range(len(data_time)):
        str = data_time[i]
        str1 = str.split(':')[2].split('.')[0]
        str2 = str.split('.')[1]
        return_str = 1000*(int(str1)-int(init_str1)) + (int(str2)-int(init_str2))
        data_time_re.append(return_str)

    date_value_abs = np.abs(data_value)
    date_re = pd.DataFrame({
        '时间':data_time_re,
        '值':date_value_abs
    })
    date_re.to_excel(os.path.join(path_output, file_output_name), index=False , header = False)

