'''
Created on 2019年4月23日

@author: rocky
'''
import logging
import logging00.submod

logger = logging.getLogger('main.mod')
logger.info('logger of mod say something...')

def testLogger():
	logger.debug('this is mod.testLogger...')
	logging00.submod.tst()
