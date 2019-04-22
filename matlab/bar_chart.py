'''
Created on 2019年3月10日
@author: rocky
'''

import plotly.plotly as py
import plotly.tools as tls

import matplotlib.pyplot as plt
import plotly
plotly.tools.set_credentials_file(username='rockywang101', api_key='7Xomd4aBgEh1Hc7oAjPs')

y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")


fig = plt.gcf()
plotly_fig = tls.mpl_to_plotly(fig)
py.iplot(plotly_fig, filename='mpl-basic-bar')