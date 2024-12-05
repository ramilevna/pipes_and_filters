# Pipes-and-Filters Messaging System

## Overview

This project implements a messaging system using the **pipes-and-filters** architectural style. The system processes user messages through a series of independent services, each connected by Unix pipes. The services include:

1. **Filter Service**: Filters out messages containing stop-words.
2. **SCREAMING Service**: Converts messages to uppercase.
3. **Publish Service**: Mocks sending an email by printing the result.

The implementation is designed to showcase the simplicity and effectiveness of pipes-and-filters for message processing. A load testing script is provided to compare the performance of this approach with an event-driven RabbitMQ-based implementation.

---

## System Components

1. **API Server** (`api_server.py`):
   - Receives JSON messages via user input.
   - Starts and connects the filter, screaming, and publish services using pipes.
2. **Filter Service** (`filter_service.py`):
   - Discards messages containing stop-words: `bird-watching`, `ailurophobia`, `mango`.
3. **SCREAMING Service** (`screaming_service.py`):
   - Converts the message text to uppercase.
4. **Publish Service** (`publish_service.py`):
   - Simulates sending an email by printing the message.
5. **Utilities** (`utils.py`):
   - Helper functions for reading from and writing to pipes.
6. **Load Testing** (`load_test.py`):
   - Measures the performance of the pipes-and-filters implementation.

---

## Prerequisites

- Python 3.6+
- Unix-based operating system (or Windows with a Unix-compatible shell).
- Optional: Use a virtual environment for dependency management.

---

## How to Run

### Start the Pipes-and-Filters System

1. Run the API server to start the system:
   ```bash
   python3 api_server.py
   
2. Follow the prompts to enter JSON messages:
	Example input:
{"alias": "professor", "text": "This is a test message"}
3.	Observe the output at each stage:
	•	Filter Service: Filters stop-words.
	•	SCREAMING Service: Converts text to uppercase.
	•	Publish Service: Prints the final message.
4. To exit the system, type exit when prompted.


Testing Individual Services

Each service can be tested independently using Unix pipes:

Filter Service

   echo '{"alias": "user", "text": "hello mango"}' | python3 filter_service.py

Expected: No output, as the message contains a stop-word.

SCREAMING Service

    echo '{"alias": "user", "text": "hello world"}' | python3 screaming_service.py

Expected:
{"alias": "user", "text": "HELLO WORLD"}

Publish Service

echo '{"alias": "user", "text": "HELLO WORLD"}' | python3 publish_service.py

Expected: Prints the mock email:

Sending email:
From user: user
Message: HELLO WORLD

Performance Testing

1.	Run the load testing script to simulate a high volume of messages:

python3 load_test.py

2.	Adjust the number of messages in load_test.py by modifying the message_count variable.
3.  Observe the performance metrics, including:
	•	Time taken to process all messages.
	•	System resource utilization (e.g., CPU, memory).

Notes on Stop-Words

Messages containing the following words will be discarded by the Filter Service:
	•	bird-watching
	•	ailurophobia
	•	mango