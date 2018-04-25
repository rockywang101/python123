'''
透過 GCM 平台發送 Android 推播
 
Created on 2018年4月25日
@author: rocky.wang
'''
import requests
import os

url = "https://android.googleapis.com/gcm/send"

headers = {
    "Content-Type": "application/json",
    "Authorization": "key=" + os.environ["GCM_AUTHORIZATION_KEY"]
}

data = {
    "to": "envTid-ONik:APA91bFPTeN2eNaKALFdqxNfWJxUe0CM8TDHoXU7zjD7r39JdgY-xXlbLwF_Xi9IMSOpSZlhuxSIwchCTAfe-q3xX6ZmiLWNcJBcVGzY-q8MpdX_AkuGQHDmhrJXD2pothxZ-iofok7a",
    "data": {
        "Title": "測試無敵推播4"
    }
}

resp = requests.post(url, headers=headers, json=data)

print(resp.json())
