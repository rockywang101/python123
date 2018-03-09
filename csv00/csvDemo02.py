'''
find Supplier X and > 600 data

Created on 2018年3月9日
@author: rocky.wang
'''
import csv
import pandas as pd

input_file = "supplier_data.csv"

with open(input_file, "r") as f1:
    reader = csv.reader(f1)
    next(reader) # don't need header
    
    for row in reader:
        cost = float(row[3].replace(",", "").strip("$"))
        if row[0] == 'Supplier X' and cost > 600:
            print(row)

''' pandas version '''
            
data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip("$").astype(float)

data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name'].str.contains('X')) \
                                                    & (data_frame['Cost'] > 600.0), :]
data_frame_value_meets_condition.to_csv("newByPondas2.csv", index=False)

print(data_frame_value_meets_condition)





