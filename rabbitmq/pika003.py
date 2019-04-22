'''
Created on 2019年4月16日
@author: rocky
'''
import pika


def on_message(channel, method_frame, header_frame, body):
	print(method_frame.delivery_tag)
	print(body)
	print()
	channel.basic_ack(delivery_tag=method_frame.delivery_tag)


def confirm_handler(frame):
	print("confirm_handler")
	print(frame)


def main():

	host = '192.168.177.143'
	credentials = pika.PlainCredentials('guest', 'guest')
	
	param = pika.ConnectionParameters(host=host, port=5672, credentials=credentials, heartbeat=300)
	connection = pika.BlockingConnection(param)
	channel = connection.channel()
	channel.confirm_delivery(callback=confirm_handler)

	msg = "Hello"
	channel.basic_publish(exchange="TEST", routing_key="test.a", body=msg)
			
	connection.close()

if __name__ == '__main__':
	main()