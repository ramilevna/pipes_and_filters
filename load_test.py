import requests
import time

def load_test(message_count):
    stop_words = ["bird-watching", "ailurophobia", "mango"]
    start_time = time.time()

    for i in range(message_count):
        if i % 3 == 0:  # Every third message contains stop word
            stop_word = stop_words[i % len(stop_words)]
            response = requests.post(
                "http://localhost:5000/send",
                json={"alias": f"user{i}", "text": f"This message contains {stop_word}"}
            )
        else:
            response = requests.post(
                "http://localhost:5000/send",
                json={"alias": f"user{i}", "text": f"This is a valid message {i}"}
            )
        
        if response.status_code != 200:
            print(f"Failed to send message {i}: {response.json()}")

    end_time = time.time()
    print(f"Processed {message_count} messages in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    load_test(15)
