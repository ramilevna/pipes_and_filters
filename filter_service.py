import sys
from utils import read_pipe, write_pipe

STOP_WORDS = {"bird-watching", "ailurophobia", "mango"}

def filter_service(input_pipe, output_pipe):
    while True:
        message = read_pipe(input_pipe)
        if not message:
            break
        if not any(word in message["text"] for word in STOP_WORDS):
            write_pipe(output_pipe, message)

if __name__ == "__main__":
    input_pipe = sys.stdin
    output_pipe = sys.stdout
    filter_service(input_pipe, output_pipe)