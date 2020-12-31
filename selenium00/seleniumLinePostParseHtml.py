'''
Run Chrome quietly

Created on 2018年4月20日
@author: rocky.wang
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium00.notifyUtils import notifyMe
import logging.config
import yaml
import traceback

loggingYamlFilepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.yml')
logging.config.dictConfig(yaml.load(open(loggingYamlFilepath, 'r'), Loader=yaml.FullLoader))
logging = logging.getLogger(__name__)
    
    
def main():

    soup = BeautifulSoup(open(f'test11223.html', encoding='utf-8'), 'html.parser')
    
    title = soup.find('h2', {'class': 'st_title-medium-bigger st-md_title-medium-biggest w-100-break'}).text.strip()
    print(title)
    
    commentBlock = soup.find(id='commentBlock')
    
    replyDivs = commentBlock.find_all('div', {'class': 'post-view pt-0 pb-3 commentList bg-purewhite pb-3 container-fluid'})
    
    print(len(replyDivs))
    for replyDiv in replyDivs:
        replyAuthorDiv = replyDiv.find('div', {'class': 'pl-0 col'}) # 包含發言者名字，時間，內文
        
        text = replyAuthorDiv.find('div', {'class': 'mt-1 mb-1'}).text.strip() # 單純內文
        print(text)
        print()
        
    # 還沒有發言者後面的留言
    # 圖片處理
    
    
    
    
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(traceback.format_exc())
        notifyMe(f'{os.path.basename(__file__)} failed')
