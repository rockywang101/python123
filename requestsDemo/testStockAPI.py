'''
Created on 2020年6月3日

@author: rocky
'''
import requests
import pandas as pd

url = "http://api.finmindtrade.com/api/v2/data"
parameter = {
    "dataset": "TaiwanStockPriceMinuteBidAsk",
    "stock_id": "4205",
}
resp = requests.get(url, params=parameter)
data = resp.json()["data"]
if data['date'] == []:
    data.pop('date', None)
data = pd.DataFrame(data)
print(data.head())

