'''
Created on 2019年4月19日
@author: rocky
'''
import logging

def initLogger():
	
	logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    handlers = [logging.FileHandler('my.log', 'w', 'utf-8'),])
	
	logger = logging.getLogger(__name__)
	
	formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
	
	console = logging.StreamHandler()
	console.setLevel(logging.INFO)
	console.setFormatter(formatter)
	logger.addHandler(console)
	
	return logger


def main():
	
	logger = initLogger()
	
	logger.debug("Hello Debug")
	logger.info("Hello Info")
	
if __name__ == '__main__':
	main()
