import sys
from utils import read_pipe

def send_email(message):
    print(f"Sending email:\nFrom user: {message['alias']}\nMessage: {message['text']}")

def publish_service(input_pipe):
    while True:
        message = read_pipe(input_pipe)
        if not message:
            break
        send_email(message)

if __name__ == "__main__":
    input_pipe = sys.stdin
    publish_service(input_pipe)