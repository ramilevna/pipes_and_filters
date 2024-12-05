import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    message["text"] = message["text"].upper()
    print(f"Message screamed: {message['text']}")  # Log the message that was converted to uppercase
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='screamed_messages')
    channel.basic_publish(exchange='', routing_key='screamed_messages', body=json.dumps(message))
    connection.close()

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='filtered_messages')  # Declare the queue to receive filtered messages
    channel.basic_consume(queue='filtered_messages', on_message_callback=callback, auto_ack=True)
    print("Screaming service running. Waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    main()
