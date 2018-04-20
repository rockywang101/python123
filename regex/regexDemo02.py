'''
Regex 字串取代

Created on 2018年4月17日
@author: rocky.wang
'''
import re

string = 'bananb'
string = re.sub(r'n.', 'NA', string)

print(string)

string = '2017/05/16'
string = re.findall(r'(\d*)\/(\d*)\/(\d*)', string)
print(string)

# replace div to span
string = "<div> 123 </div>"
string = re.sub(r'(<\/?)(div)(>)', r'\1span\3', string)
print(string)






