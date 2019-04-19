'''
Created on 2019年4月18日
@author: rocky.wang
'''
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import time
from logging00.submodule import pp


def initLogger():
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)
	
	formatter = logging.Formatter('%(asctime)s %(levelname)s\t%(module)s - %(message)s')
	
	streamHandler = logging.StreamHandler()
	streamHandler.setFormatter(formatter)
	logger.addHandler(streamHandler)
	
	debugFileHandler = TimedRotatingFileHandler(os.path.join(os.getcwd(), 'debug.log'), when="D", interval=1, backupCount=30)
	debugFileHandler.setFormatter(formatter)
	debugFileHandler.setLevel(logging.INFO)
	logger.addHandler(debugFileHandler)

	infoFileHandler = TimedRotatingFileHandler(os.path.join(os.getcwd(), 'info.log'), when="D", interval=1, backupCount=180)
	infoFileHandler.setFormatter(formatter)
	infoFileHandler.setLevel(logging.DEBUG)
	logger.addHandler(infoFileHandler)


def main():
	initLogger()
	
	process()
	
	pp()
	
	
def process():
	logger = logging.getLogger(__name__)
	
	for i in range(3):
		print("print", i)
		logger.debug("debug " + str(i))
		logger.info("info " + str(i))
		time.sleep(0.5)


if __name__ == "__main__":
	main()
