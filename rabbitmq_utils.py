import pika

def get_rabbitmq_channel(host='localhost'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel = connection.channel()
    return channel

def setup_queue(channel, queue_name):
    channel.queue_declare(queue=queue_name, durable=True)