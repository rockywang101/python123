'''
Created on 2020年2月13日
@author: rocky
'''

import yaml

with open('a.yaml') as fp:
    data1 = yaml.load(fp)
with open('b.yaml') as fp:
    data2 = yaml.load(fp)
    
print(data1)
print("----------")
print(data2)

def dict_merge(dict1, dict2):
    for k, v in iter(dict2.items()):
        if (k in dict1 and isinstance(dict1[k], dict) and isinstance(dict2[k], dict)):
            dict_merge(dict1[k], dict2[k])
        else:
            dict1[k] = dict2[k]
            
            
            
            
dict_merge(data1, data2)

print("\nafeter merge-----------")
print(data1)
print("----------")
print(data2)

print(data1['a']['c'])
print(data1['a']['d']['y'])