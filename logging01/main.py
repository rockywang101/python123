'''
Created on 2019年4月23日
@author: rocky
'''
import logging.config
import yaml
from logging01.service01 import dosomething
from logging01.sub.subservice01 import sayHello

logging.config.dictConfig(yaml.load(open('logging.yml', 'r'), Loader=yaml.FullLoader))

logger = logging.getLogger(__name__)
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

dosomething()

sayHello('John')



