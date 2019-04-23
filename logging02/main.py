'''
try gmail logging, not completed

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



