'''
Created on 2020年5月4日
@author: rocky
'''

# pip3 install fix-yahoo-finance
# pip3 install yfinance --upgrade --no-cache-dir

import datetime
#import fix_yahoo_finance as yf
import yfinance as yf
from dateutil.relativedelta import relativedelta

yf.pdr_override()
start = datetime.datetime.now() - relativedelta(days=7)
end =  datetime.datetime.now()

# stock_yf = yf.download('1101.TW', start, end)
stock_yf = yf.download('6026.TWO', start, end)
print(stock_yf)

