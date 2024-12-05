import pika
import json

def send_email(message):
    print(f"Sending email:\nFrom user: {message['alias']}\nMessage: {message['text']}")

def callback(ch, method, properties, body):
    message = json.loads(body)
    send_email(message)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='screamed_messages')
    channel.basic_consume(queue='screamed_messages', on_message_callback=callback, auto_ack=True)
    print("Publish service running. Waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    main()
