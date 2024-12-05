import sys
from utils import read_pipe, write_pipe

def screaming_service(input_pipe, output_pipe):
    while True:
        message = read_pipe(input_pipe)
        if not message:
            break
        message["text"] = message["text"].upper()
        write_pipe(output_pipe, message)

if __name__ == "__main__":
    input_pipe = sys.stdin
    output_pipe = sys.stdout
    screaming_service(input_pipe, output_pipe)