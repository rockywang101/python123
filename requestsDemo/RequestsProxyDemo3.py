'''
Created on 2020年5月4日
@author: rocky
'''
import requests
import csv

url = "http://httpbin.org/ip"
 
r = requests.get(url, verify=False)
print(r)
print(r.text)
print('\n') 

proxy_host = '185.186.245.227'
proxy_port = 80
proxy_auth = ":"
proxies = {
    "http": f"http://{proxy_auth}@{proxy_host}:{proxy_port}",
    "https": f"https://{proxy_auth}@{proxy_host}:{proxy_port}"
}

#r = requests.get(url, proxies=proxies, verify=False)
r = requests.get(url, proxies=proxies)
 
print(r)
print(r.text)
print('\n') 


url = 'https://httpbin.org/ip'

with requests.Session() as se:
    r = se.get(url, proxies=proxies)
    print(r)

r = requests.get(url, proxies=proxies)
 
print(r)
print(r.text)
print('\n') 
    