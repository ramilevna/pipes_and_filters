import pika
import json

STOP_WORDS = {"bird-watching", "ailurophobia", "mango"}

def callback(ch, method, properties, body):
    message = json.loads(body)
    # Check if the message contains any stop words
    if not any(word in message["text"] for word in STOP_WORDS):
        print(f"Message passed filter: {message['text']}")  # Log the message that passed the filter
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='filtered_messages')
        channel.basic_publish(exchange='', routing_key='filtered_messages', body=json.dumps(message))
        connection.close()
    else:
        print(f"Message filtered out: {message['text']}")  # Log the message that was filtered out

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='messages')  # Declare the queue to receive incoming messages
    channel.basic_consume(queue='messages', on_message_callback=callback, auto_ack=True)
    print("Filter service running. Waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    main()
