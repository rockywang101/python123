'''
Created on 2019年4月24日
@author: rocky
'''
import logging

def sayHello(name):
	logger = logging.getLogger(__name__)
	logger.info(f'Hello {name}')
