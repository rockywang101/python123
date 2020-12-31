'''

filter really OK proxy list

Created on 2020年5月4日
@author: rocky
'''
import requests
import csv

url = "http://httpbin.org/ip"
 
rowList = list(csv.reader(open('proxyList.csv', encoding='utf-8'))) 

resultList = []

cnt = 0
for row in rowList[1:]:
    cnt += 1
    print(cnt)

    proxy_host = row[0]
    proxy_port = row[1]
    proxy_auth = ':'
    proxies = {
        'http': f'http://{proxy_auth}@{proxy_host}:{proxy_port}/',
        'https': f'https://{proxy_auth}@{proxy_host}:{proxy_port}'
    }
    
    print(f'Get with proxy: {proxies}')
    try:
        r = requests.get(url, proxies=proxies)
        if r.status_code == 200:
            print('OK')
            with open('proxyListOK.csv', 'a', encoding='utf-8', newline='') as f:
                csv.writer(f).writerow(row)
            resultList.append(row)
        else:
            print('Fail')
    except Exception as e:
        print(e)

print('completed.')
