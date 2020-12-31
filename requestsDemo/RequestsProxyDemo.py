'''
Created on 2020年5月4日
@author: rocky
'''
import requests
import csv

url = "http://httpbin.org/ip"
 
r = requests.get(url, verify=False)
print(f"GET {url} with no proxy")
print(r)
print(r.text)
print("------------------------------")
 
print(f"GET {url} with proxy")
 
rowList = list(csv.reader(open('proxyList.csv', encoding='utf-8'))) 

row = rowList[4]
 
proxy_host = row[0]
proxy_port = row[1]
proxy_auth = ":"
proxies = {
    "https": f"https://{proxy_auth}@{proxy_host}:{proxy_port}",
    "http": f"http://{proxy_auth}@{proxy_host}:{proxy_port}/"
}

print(proxies)
 
r = requests.get(url, proxies=proxies, verify=False)
 
if r.status_code == 200:
    print(r)
    print(r.text)
else:
    print("Fail")
    print(r)
    print(r.text)


    