'''
find datas in 1/20/14, 1/30/14

Created on 2018年3月9日
@author: rocky.wang
'''
import csv
import pandas as pd

input_file = "supplier_data.csv"
output_file = "newByCsv.csv"
output_file_pandas = "newByPandas.csv"

important_dates = ['1/20/14', '1/30/14']

with open(input_file, "r") as f1, open(output_file, "w", newline="") as f2:
    reader = csv.reader(f1)
    writer = csv.writer(f2)
    next(reader) # don't need header
    
    for row in reader:
        if row[4] in important_dates:
            writer.writerow(row)
            
''' pandas version '''
data_frame = pd.read_csv(input_file)

dataFrameInSet = data_frame.loc[data_frame["Purchase Date"].isin(important_dates)]

dataFrameInSet.to_csv(output_file_pandas, index=False)

            
            
            
            

