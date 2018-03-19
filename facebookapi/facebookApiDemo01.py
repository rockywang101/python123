'''
Demo fetch Facebook FanPage data

Created on 2018年3月19日
@author: rocky.wang
'''

'''
Created on 2018年3月13日
@author: rocky.wang
'''
import requests
import json

fanPageId = "arsin168"
fanPageId = "emily0806"

fields = "id, posts.limit"
token = "EAACEdEose0cBALeiXO3ZB7o7bndS2jOECuzyGXjiDFPcXFONQ9SjjyJQspoxaBcZA1TT0wRtmCVfEl44EMjAZB8MgESiMMJIo5oPbECCBwnC2jmk7eJgZA0oCzoGYqlZB0siLBwhxMl4uBsSXooavM6kdnW60LwVIQ34P9IycELY8gKY3tZAaZBPgufbyRRWnMGQKnL8QNruQZDZD"

url = 'https://graph.facebook.com/v2.10/{}?fields={}&access_token={}'.format(fanPageId, fields, token)

print(url)


def fetchPostPictures(postId):
    fields = "attachments"
    url = 'https://graph.facebook.com/v2.10/{}?fields={}&access_token={}'.format(postId, fields, token)
    response = requests.get(url)
    js = json.loads(response.text)
    print(js)
    picUrlList = []
    for data in js["attachments"]["data"][0]["subattachments"]["data"]:
        picUrlList.append(data["media"]["image"]["src"])
    return picUrlList

response = requests.get(url)

js = json.loads(response.text)

print(js)

cnt = 0
i = 0
for data in js["posts"]["data"]:
    i += 1
    if i > 3:
        continue
    try:
        cnt += 1
        message = data['message']
        print(cnt)
        print(data["id"])
        print(message)
        print()
        
        picUrlList = fetchPostPictures(data["id"])
        
    except:
        print(data)
    
print("-------------------------")
nextUrl = js["posts"]["paging"]["next"] 


