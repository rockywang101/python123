'''
Created on 2018年3月2日
@author: rocky.wang
'''
import csv

input_file = "supplier_data.csv"
output_file = "new.csv"

with open(input_file, "r") as f1, open(output_file, "w", newline="") as f2:
    
    reader = csv.reader(f1)
    writer = csv.writer(f2)

    for row in reader:
        writer.writerow(row)
    
        
""" pandas version """
import pandas as pd

output_file = "newByPandas.csv"

data_frame = pd.read_csv(input_file)
data_frame.to_csv(output_file, index=False)
