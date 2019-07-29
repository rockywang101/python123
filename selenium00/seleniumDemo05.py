'''
樂活五線譜 0050 截圖

Created on 2018年4月20日
@author: rocky.wang
'''
# pip3 install pillow
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time


options = Options()
#options.add_argument("--headless")
driver = webdriver.Firefox(options=options) # 把 geckodriver.exe 檔案放到 C:\Windows\System32\ 下即可

# 設定大小是為了想控制後面截圖座標，但後面截圖還是與我理解的不同，因為 x 要超過 1024 才會截到完整的圖
driver.set_window_size(1024, 768)

driver.get("http://invest.wessiorfinance.com/notation.html")

elem = driver.find_element_by_id("Stock")
elem.send_keys("0050")

elem.send_keys(Keys.RETURN)

print("wait for picture")
time.sleep(5) # sleep 是較差的作法，應該可以改成 while 去等待其他繒圖的 html 碼出現即可進行截圖

im = ImageGrab.grab(bbox=(300, 100, 1250, 650))
im.save('0050.jpg', 'jpeg')

driver.close()

# 再配合 line notify 發本機端的圖即可