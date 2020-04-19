'''
Created on 2020年2月13日
@author: rocky
'''

import yaml

with open('b.yaml') as fp:
    data = yaml.load(fp)

v = data['vvv']
print(f"{v} {type(v)}")

for key in v:
    print(f"{key} : {v[key]}")
