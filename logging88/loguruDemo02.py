'''
Created on 2018年10月9日
@author: rocky.wang
'''

import datetime

from loguru import logger
import sys

logger.remove()
logger.add(takeSomeTimeTask   sys.stdout, 
    colorize=True, 
    level='TRACE', 
    format='<level>{time:YYYY-MM-DD HH:mm:ss} {level}\t{message}</level>'
)

logger.add(takeSomeTimeTask   f'{datetime.date.today():%Y%m%d}.log',
    rotation='1 day',
    retention='7 days',
    level='TRACE',
    format='<level>{time:YYYY-MM-DD HH:mm:ss} {level}\t{message}</level>'
)


logger.trace('I am TRACE Level')
logger.debug('I am DEBUG Level')
logger.info('I am INFO Level')
logger.success('I am SUCCESS Level')
logger.warning('I am WARNING Level')
logger.error('I am ERROR Level')
logger.critical('I am CRITICAL Level')

