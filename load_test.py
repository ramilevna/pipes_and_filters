import time
import subprocess

def load_test(message_count):
    start_time = time.time()

    with subprocess.Popen(
        ["python3", "api_server.py"], stdin=subprocess.PIPE, text=True
    ) as api_process:
        for i in range(message_count):
            api_process.stdin.write(f'{{"alias": "user{i}", "text": "message {i}"}}\n')
            api_process.stdin.flush()
        api_process.stdin.write("exit\n")
        api_process.stdin.flush()
        api_process.wait()

    end_time = time.time()
    print(f"Processed {message_count} messages in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    load_test(1000)