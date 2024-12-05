import sys
import json
import subprocess

def api_server(pipe):
    print("API server running. Send messages as JSON in format {'alias': '...', 'text': '...'}")
    while True:
        try:
            data = input("Enter message (or type 'exit' to stop): ")
            if data.strip().lower() == "exit":
                break
            message = json.loads(data)
            pipe.write(json.dumps(message) + "\n")
            pipe.flush()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    with subprocess.Popen(
        ["python3", "filter_service.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    ) as filter_process, subprocess.Popen(
        ["python3", "screaming_service.py"],
        stdin=filter_process.stdout,
        stdout=subprocess.PIPE,
        text=True,
    ) as screaming_process, subprocess.Popen(
        ["python3", "publish_service.py"],
        stdin=screaming_process.stdout,
        text=True,
    ) as publish_process:
        api_server(filter_process.stdin)