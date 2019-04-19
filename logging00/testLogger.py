'''
Created on 2019年4月18日
@author: rocky.wang
'''
import logging
import os
from logging.handlers import TimedRotatingFileHandler, SMTPHandler
import time
import logging00.submodule as submodule
import traceback


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
	
	fromaddr = 'no-reply@ehsn.com.tw'
	toaddrs = ['rocky.wang@ehsn.com.tw']
	subject = 'System Error From Logging'
	smtpHandler = SMTPHandler('mail01.etzone.net', fromaddr, toaddrs, subject)
	smtpHandler.setFormatter(formatter)
	smtpHandler.setLevel(logging.ERROR)
	logger.addHandler(smtpHandler)
	
	return logger

def main():
	try:
		logger = initLogger()
	
		submodule.pp()
		
		process()
	except:
		logger.error(traceback.format_exc())
	
	
def process():
	logger = logging.getLogger(__name__)
	
	logger.debug("debug in main")
	logger.info("info in main")
	
	submodule.causeError()
	

if __name__ == "__main__":
	main()
		
		