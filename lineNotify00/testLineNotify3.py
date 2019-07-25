import requests
 
"""
發送 Line Notify 訊息與網路上的圖片
"""
def lineNotify(token, msg, imageThumbnail, imageFullsize):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
   
    payload = {'message': msg, 'imageThumbnail': imageThumbnail, 'imageFullsize': imageFullsize}
    return requests.post(url, headers = headers, params = payload)
 
 
token = "xxxxxxxxxxxxxxxxxxxxxxxx"
msg = "賣當勞都是維尼"
picURI = "https://dvblobcdnjp.azureedge.net//Content/Upload/Popular/Images/2017-07/fa2c3d72-7fad-4ccf-9857-e90af952b956_m.jpg"
 
r = lineNotify(token, msg, picURI, picURI)
print(r.text)