'''
Optical Character Recognition，OCR Demo

tesseract-ocr/tesseract Wiki · GitHub 依照自己電腦的作業系統安裝 tesseract
pip install pillow
pip install pytesseract

辯視度超低，misc2.png 辯視錯誤，misc1.png 與 misc3.png 都是空白沒結果

Created on 2020年5月4日
@author: rocky
'''
from PIL import Image
import pytesseract

# 另一個解法是把路徑加入 PATH，記得是安裝的 win64 檔，不是 pip 安裝的 pytesseract 檔
pytesseract.pytesseract.tesseract_cmd = (
    r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
)

img = Image.open('misc2.png')
ans = pytesseract.image_to_string(img)
print(ans)




