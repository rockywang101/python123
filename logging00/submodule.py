'''
Created on 2019年4月19日
@author: rocky.wang
'''
import logging

def main():
	print("main in submodule")
	pp()

def pp():
	logger = logging.getLogger("__main__.submodule")
	logger.info("PPPPPPP")

if __name__ == "__main__":
	print("if __name__ == __main__ in submodule")
	main()