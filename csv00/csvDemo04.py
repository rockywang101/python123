'''
find datas by regular expression

Created on 2018年3月9日
@author: rocky.wang
'''
import csv, re, sys
import pandas as pd

input_file = "supplier_data.csv"
output_file = "newByCsv.csv"
output_file_pandas = "newByPandas.csv"

# pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)

with open(input_file, "r") as f1, open(output_file, "w", newline="") as f2:
    reader = csv.reader(f1)
    writer = csv.writer(f2)
    writer.writerow(next(reader))
    
    



            
''' pandas version '''

            
            
            
            

