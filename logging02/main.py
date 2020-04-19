'''
gmail logging

pyyaml 似乎不支援 tuple，所以在 loggin.yml 檔裡 mailhost 與 credentials 都要特別寫成 list 的型態才能在 init 的時候正確被解析出值g


Created on 2019年4月23日
@author: rocky
'''
import logging.config
import yaml

logging.config.dictConfig(yaml.load(open('logging.yml', 'r'), Loader=yaml.FullLoader))

logger = logging.getLogger(__name__)
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

try:
	5 / 0
except:
	logger.exception("Exception occurred")



