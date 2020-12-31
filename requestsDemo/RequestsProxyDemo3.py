'''
Created on 2020年5月4日
@author: rocky
'''
import requests

url = "http://httpbin.org/ip"
 
r = requests.get(url, verify=False)
print(r)
print(r.text)
print('\n') 

proxyHost = '23.227.199.114:3128'
proxies = {
    'http': f'http://{proxyHost}',
    'https': f'https://{proxyHost}'
}

r = requests.get(url, proxies=proxies)
 
print(r)
print(r.text)
print('\n') 


url = 'https://httpbin.org/ip'

# with requests.Session() as se:
#     r = se.get(url, proxies=proxies)
#     print(r)

r = requests.get(url, proxies=proxies)
 
print(r)
print(r.text)
print('\n') 
    