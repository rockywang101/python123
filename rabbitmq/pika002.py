'''
Created on 2019年4月15日

@author: rocky
'''
import pika


def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    print()
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


host = '192.168.177.143'
credentials = pika.PlainCredentials('guest', 'guest')

param = pika.ConnectionParameters(host=host, port=5672, credentials=credentials, heartbeat=300)
connection = pika.BlockingConnection(param)
channel = connection.channel()
channel.basic_consume('test_queue', on_message)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()