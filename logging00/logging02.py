'''
Created on 2019年4月23日
@author: rocky
'''
import logging.config
import yaml

logging.config.dictConfig(yaml.load(open('logging.yml', 'r'), Loader=yaml.FullLoader))

logger = logging.getLogger('simpleExample')
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
