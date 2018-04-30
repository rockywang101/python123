'''
發送 Line Notify 訊息

Created on 2018年4月30日
@author: rocky.wang
'''
import requests
def lineNotify(token, msg):
    
    url = "https://notify-api.line.me/api/notify"
    
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
   
    payload = {'message': msg}
    r = requests.post(url, headers = headers, params = payload)
    
    print(r.status_code)
    print(r.headers)
    
    return r.status_code

token = "2D7IaxfEThWOFQJUu6Wpp8kliclIW1o7C0VaDCiaR7V"
msg = "Hello Python"

lineNotify(token, msg)
