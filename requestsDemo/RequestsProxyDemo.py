'''
Created on 2020年5月4日
@author: rocky
'''
import requests

url = "http://httpbin.org/ip"
proxy_host = "35.238.200.65"
proxy_port = "8080"
proxy_auth = ":"
proxies = {
    "https": f"https://{proxy_auth}@{proxy_host}:{proxy_port}",
    "http": f"http://{proxy_auth}@{proxy_host}:{proxy_port}/"
}

r = requests.get(url, verify=False)
print(f"GET {url} no proxy")
print(r)
print(r.text)
print("------------------------------")

r = requests.get(url, proxies=proxies, verify=False)
print(f"GET {url} with proxy")
print(r)
print(r.text)