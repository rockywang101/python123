'''
Created on 2019年4月13日
@author: rocky
'''
import pika


def main():

	host = '192.168.177.143'
	credentials = pika.PlainCredentials('guest', 'guest')
	
	param = pika.ConnectionParameters(host=host, port=5672, credentials=credentials, heartbeat=300)
	connection = pika.BlockingConnection(param)
	channel = connection.channel()

	msg = "Hello"
	channel.basic_publish(exchange="TEST", routing_key="test.a", body=msg)
			
	connection.close()

if __name__ == '__main__':
	main()