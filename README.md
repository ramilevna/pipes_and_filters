# README.md

# Pipes-and-Filters Messaging System

## Overview

This project demonstrates a **pipes-and-filters** architecture for processing user messages. The system sequentially processes messages through independently deployable services, connected via Unix pipes. Each service performs a specific function:

1. **Filter Service**: Removes messages containing stop-words.
2. **SCREAMING Service**: Converts messages to uppercase.
3. **Publish Service**: Simulates sending an email.

The project also provides a **load testing script** for evaluating the performance of the pipes-and-filters model.

---

## System Architecture

The system consists of the following components:

1. **API Server** (`api_server.py`):
    - Acts as the entry point for user messages.
    - Starts and connects the services using Unix pipes.
2. **Filter Service** (`filter_service.py`):
    - Filters out messages containing any of the stop-words:
        - `bird-watching`
        - `ailurophobia`
        - `mango`
3. **SCREAMING Service** (`screaming_service.py`):
    - Converts all message text to uppercase.
4. **Publish Service** (`publish_service.py`):
    - Simulates sending an email, printing the final processed message.
5. **Utilities** (`utils.py`):
    - Provides helper functions for reading and writing data between pipes.
6. **Load Testing Script** (`load_test.py`):
    - Simulates a high volume of messages to assess the performance of the system.

---

## Prerequisites

- Python 3.6 or newer.
- Unix-based operating system (or Windows with a Unix compatibility layer like WSL or Cygwin).
- Optional: A virtual environment for managing dependencies.

---

## How to Run the System

### **Starting the Pipes-and-Filters System**

1. **Run the API server**:
    
    `python3 api_server.py`
    
2. **Follow the prompts** to enter messages in JSON format:
*Example input:*
    
    `{"alias": "professor", "text": "This is a test message"}`
    
3. **Observe the output**:
    - Filter Service: Filters messages with stop-words.
    - SCREAMING Service: Converts text to uppercase.
    - Publish Service: Prints the final processed message as a mock email.
4. To exit the system, type `exit` when prompted.

---

### **Testing Individual Services**

Each service can be tested independently using Unix pipes:

### **Filter Service**

`echo '{"alias": "user", "text": "hello mango"}' | python3 filter_service.py`

**Expected Output**: No output, as the message contains a stop-word.

---

### **SCREAMING Service**

`echo '{"alias": "user", "text": "hello world"}' | python3 screaming_service.py`

**Expected Output**:

`{"alias": "user", "text": "HELLO WORLD"}`

---

### **Publish Service**

`echo '{"alias": "user", "text": "HELLO WORLD"}' | python3 publish_service.py`

**Expected Output**:

`Sending email:
From user: user
Message: HELLO WORLD`

---

### **Performance Testing**

1. **Run the load testing script** to simulate a high message volume:
    
    `python3 load_test.py`
    
2. **Adjust the number of messages** in the script by modifying the `message_count` variable.
3. Observe performance metrics, including:
    - Time taken to process all messages.
    - System resource usage (CPU, memory, etc.).

---

## System Notes

1. **Stop-Words**:
    - Messages containing the following words are discarded by the Filter Service:
        - `bird-watching`
        - `ailurophobia`
        - `mango`
2. **Scalability**:
    - This implementation uses Unix pipes for inter-service communication.
    - Each service is an independent process and can be scaled horizontally by deploying multiple instances.
3. **Debugging**:
    - To debug individual services, you can direct input to a service using a pipe and observe the output as shown above.

---

## Future Enhancements

- **Event-Driven Model**: Reimplement the system with RabbitMQ for distributed and asynchronous communication.
- **Error Handling**: Add robust error-handling mechanisms for unexpected inputs.
- **Logging**: Include centralized logging for better observability.
