# sender.py
import pika
import json
import rabbitmq_utils

def send_collateral_request(channel, queue_name, request_data):
    message = json.dumps(request_data)
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)  # make message persistent
    )

if __name__ == "__main__":
    queue_name = 'collateral_requests'
    channel = rabbitmq_utils.get_rabbitmq_channel()
    rabbitmq_utils.setup_queue(channel, queue_name)

    # Example collateral request
    request_data = {
        'transaction_type': 'settle_to_cash',
        'amount': 1000,
        'currency': 'USD',
        'client_id': 'client_123'
    }
    send_collateral_request(channel, queue_name, request_data)