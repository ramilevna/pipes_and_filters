import pika
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def send_to_queue(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='messages')
    channel.basic_publish(exchange='', routing_key='messages', body=json.dumps(message))
    connection.close()

@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        alias = data.get('alias')
        text = data.get('text')
        if not alias or not text:
            return jsonify({"error": "Alias and text are required"}), 400
        message = {"alias": alias, "text": text}
        send_to_queue(message)
        return jsonify({"message": "Message sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
