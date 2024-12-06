# README.md

# Pipes-and-Filters Messaging System

## Overview

This is a message processing system that follows the **Pipes-and-Filters** architectural pattern using **RabbitMQ** as a message broker. The system consists of several independently deployable services that process messages sequentially. Each service performs a specific task (filtering, converting text to uppercase, and publishing messages).

The system is split into four services, each performing a specific function. These services are connected using RabbitMQ queues, where each service processes the message and passes it to the next service.

- **User-facing REST API Server**: Receives POST requests with message data (alias and text).
- **Filter Service**: Filters messages for stop words. Messages containing any of the stop words are discarded.
- **Screaming Service**: Converts the message text to uppercase.
- **Publish Service**: Simulates sending an email to a list of users with the processed message.

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
5. **Load Testing Script** (`load_test.py`):
    - Simulates a stream of messages (valid and not) to assess the performance of the system.

---

## Prerequisites

- Python 3.7 or newer.
- RabbitMQ server (running locally or remotely)

---

## Python Libraries

- `pika` (for RabbitMQ communication)
- `flask` (for the REST API)
- `requests` (for load testing)

## How to Run the System

For running the system, the user should download Erlang and RabbitMQ.

Once both Erlang and RabbitMQ have been installed, a RabbitMQ node can be started as a Windows service. The RabbitMQ service starts automatically. RabbitMQ Windows service can be managed from the Start menu.

### **Starting the system**

To run the system the user should run all the scripts in separate terminals.

1. **Start the API server**:
    
    `python api_server.py`
    
    This will start the REST API server at http://localhost:5000.

2. **Start the Filter service**:

    `python filter_service.py`
    
    The service will read messages from the messages queue and pass valid ones to the filtered_messages queue.

3. **Start the Screaming service**:
    
    `python screaming_service.py`
    
    This service will read messages from the filtered_messages queue, convert them to uppercase, and forward them to the screamed_messages queue.

3. **Start the Publish service**:
    
    `python publish_service.py`
    
    This service will read messages from the screamed_messages queue and simulate sending an email by printing the output.

---

### **Performance Testing**

1. **Run the load testing script** to simulate a high message volume:
    
    `python load_test.py`
    
2. **Custom Load Test**:
To adjust the number of messages sent in the load test, modify the number in the `load_test(15)` function call within the load_test.py script.

---

## Performance and Scalability
This system can be scaled by:

- **Adding More Services**:  More filters can be added to the pipeline to perform additional processing steps.
- **Horizontal Scaling**: Running multiple instances of each service behind a load balancer or using a message queue for scalability.

## Comparing Pipes-and-Filters and Event-Driven Systems:
The **Pipes-and-Filters** pattern enables clear separation of concerns, while an event-driven system (using **RabbitMQ**) provides asynchronous message processing, making it more suitable for scenarios where services need to process data concurrently or with varying loads.

---

## Conclusion

This system is designed using the **Pipes-and-Filters** architectural pattern and **RabbitMQ** as the message broker. Each service (filter) is independent, and messages flow through the system sequentially, with transformations occurring at each step. The system is modular, extensible, and scalable, making it suitable for various message processing use cases.

# DEMO

https://drive.google.com/file/d/1nIcUwDDrR7zj-G2oBLpWHy05CVDk2E_w/view?usp=sharing
