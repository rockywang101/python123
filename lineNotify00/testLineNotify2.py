import requests, os
 
"""
發送 Line Notify 訊息與本機圖片
"""
def lineNotify(token, msg, picURI):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
   
    payload = {'message': msg}
    files = {'imageFile': open(picURI, 'rb')}
    return requests.post(url, headers = headers, params = payload, files = files)
 
 
token = os.environ["LINE_TEST_TOKEN"]
msg = "Hello Python"
picURI = "/home/rocky.wang/圖片/12438986_730224517114571_319381315566098386_n.jpg"
 
r = lineNotify(token, msg, picURI)
print(r.text)