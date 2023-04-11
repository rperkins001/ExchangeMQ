# receiver.py
import json
import pika
import rabbitmq_utils

def process_collateral_request(channel, method, properties, body):
    request_data = json.loads(body)
    print(f"Received collateral request: {request_data}")

    # Process the request based on transaction_type
    transaction_type = request_data['transaction_type']
    if transaction_type == 'settle_to_cash':
        # Process settle to cash transaction
        pass
    # Add other transaction types here

    channel.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == "__main__":
    queue_name = 'collateral_requests'
    channel = rabbitmq_utils.get_rabbitmq_channel()
    rabbitmq_utils.setup_queue(channel, queue_name)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=process_collateral_request)

    print('Waiting for collateral requests...')
    channel.start_consuming()