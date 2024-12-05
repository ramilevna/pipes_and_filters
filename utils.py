import json

def read_pipe(pipe):
    try:
        line = pipe.readline()
        return json.loads(line.strip()) if line else None
    except Exception as e:
        print(f"Error reading from pipe: {e}")
        return None

def write_pipe(pipe, message):
    try:
        pipe.write(json.dumps(message) + "\n")
        pipe.flush()
    except Exception as e:
        print(f"Error writing to pipe: {e}")