# Socket Programming in Python

# Python에서의 소켓 프로그래밍

## Introduction

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to form a connection. The client reaches out to the server, and the server creates the listener socket.

Python's `socket` module provides a powerful interface for network programming. This guide covers the basics of socket programming in Python, focusing on TCP and UDP implementations.

## 소개

소켓 프로그래밍은 네트워크 상의 두 노드를 연결하여 서로 통신하게 하는 방법입니다. 하나의 소켓(노드)은 특정 IP의 특정 포트에서 리스닝하고, 다른 소켓은 연결을 형성하기 위해 접속합니다. 클라이언트는 서버에 접속하고, 서버는 리스너 소켓을 생성합니다.

Python의 `socket` 모듈은 네트워크 프로그래밍을 위한 강력한 인터페이스를 제공합니다. 이 가이드에서는 TCP 및 UDP 구현에 중점을 두고 Python에서의 소켓 프로그래밍 기초를 다룹니다.

## Basic Concepts

### What is a Socket?

A socket is an endpoint of a two-way communication link between two programs running on the network. Sockets are bound to specific ports, allowing communication between applications running on different hosts.

### Socket Types

The two primary socket types used in Python are:

1. **Stream Sockets (SOCK_STREAM)**: Provide reliable, two-way, connection-based byte streams. They use TCP (Transmission Control Protocol), which ensures that data arrives in order without errors.

2. **Datagram Sockets (SOCK_DGRAM)**: Support connectionless, unreliable messages of a fixed maximum length. They use UDP (User Datagram Protocol), which is faster but less reliable than TCP.

### Socket Families

Python supports various socket families, but the most common are:

- `AF_INET`: IPv4 Internet protocols
- `AF_INET6`: IPv6 Internet protocols 
- `AF_UNIX`: Local communication (Unix domain sockets)

## 기본 개념

### 소켓이란 무엇인가?

소켓은 네트워크에서 실행 중인 두 프로그램 간의 양방향 통신 링크의 엔드포인트입니다. 소켓은 특정 포트에 바인딩되어 다른 호스트에서 실행되는 애플리케이션 간의 통신을 가능하게 합니다.

### 소켓 유형

Python에서 사용되는 두 가지 주요 소켓 유형은 다음과 같습니다:

1. **스트림 소켓(SOCK_STREAM)**: 신뢰할 수 있는 양방향, 연결 기반 바이트 스트림을 제공합니다. TCP(Transmission Control Protocol)를 사용하며, 이는 데이터가 오류 없이 순서대로 도착하는 것을 보장합니다.

2. **데이터그램 소켓(SOCK_DGRAM)**: 고정된 최대 길이의 연결 없는, 신뢰할 수 없는 메시지를 지원합니다. UDP(User Datagram Protocol)를 사용하며, 이는 TCP보다 빠르지만 신뢰성이 떨어집니다.

### 소켓 패밀리

Python은 다양한 소켓 패밀리를 지원하지만, 가장 일반적인 것은 다음과 같습니다:

- `AF_INET`: IPv4 인터넷 프로토콜
- `AF_INET6`: IPv6 인터넷 프로토콜
- `AF_UNIX`: 로컬 통신(Unix 도메인 소켓)

## TCP Socket Programming

### TCP Server

Here's a basic example of a TCP server:

```python
import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('localhost', 10000)
server_socket.bind(server_address)

# Listen for incoming connections (max 5 queued connections)
server_socket.listen(5)
print(f"Server is listening on {server_address}")

try:
    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        try:
            # Receive and send back data
            while True:
                data = client_socket.recv(1024)
                if data:
                    print(f"Received: {data.decode('utf-8')}")
                    client_socket.sendall(f"Echo: {data.decode('utf-8')}".encode('utf-8'))
                else:
                    print(f"No more data from {client_address}")
                    break
                
        finally:
            # Clean up the connection
            client_socket.close()
            
except KeyboardInterrupt:
    print("Server is shutting down")
finally:
    server_socket.close()
```

### TCP Client

Here's a basic example of a TCP client:

```python
import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('localhost', 10000)
print(f"Connecting to {server_address}")
client_socket.connect(server_address)

try:
    # Send data
    message = "Hello, server!"
    print(f"Sending: {message}")
    client_socket.sendall(message.encode('utf-8'))
    
    # Receive the response
    data = client_socket.recv(1024)
    print(f"Received: {data.decode('utf-8')}")
    
finally:
    # Clean up the connection
    print("Closing socket")
    client_socket.close()
```

## TCP 소켓 프로그래밍

### TCP 서버

다음은 기본적인 TCP 서버의 예입니다:

```python
import socket

# TCP/IP 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓을 주소와 포트에 바인딩
server_address = ('localhost', 10000)
server_socket.bind(server_address)

# 들어오는 연결 대기(최대 5개의 대기 연결)
server_socket.listen(5)
print(f"서버가 {server_address}에서 리스닝 중입니다")

try:
    while True:
        # 연결 대기
        client_socket, client_address = server_socket.accept()
        print(f"{client_address}로부터의 연결")
        
        try:
            # 데이터 수신 및 반송
            while True:
                data = client_socket.recv(1024)
                if data:
                    print(f"수신: {data.decode('utf-8')}")
                    client_socket.sendall(f"에코: {data.decode('utf-8')}".encode('utf-8'))
                else:
                    print(f"{client_address}로부터 더 이상의 데이터가 없습니다")
                    break
                
        finally:
            # 연결 정리
            client_socket.close()
            
except KeyboardInterrupt:
    print("서버가 종료됩니다")
finally:
    server_socket.close()
```

### TCP 클라이언트

다음은 기본적인 TCP 클라이언트의 예입니다:

```python
import socket

# TCP/IP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓을 서버에 연결
server_address = ('localhost', 10000)
print(f"{server_address}에 연결 중")
client_socket.connect(server_address)

try:
    # 데이터 전송
    message = "안녕하세요, 서버!"
    print(f"전송: {message}")
    client_socket.sendall(message.encode('utf-8'))
    
    # 응답 수신
    data = client_socket.recv(1024)
    print(f"수신: {data.decode('utf-8')}")
    
finally:
    # 연결 정리
    print("소켓 닫는 중")
    client_socket.close()
```

## UDP Socket Programming

### UDP Server

Here's a basic example of a UDP server:

```python
import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_address = ('localhost', 10000)
server_socket.bind(server_address)
print(f"UDP server is up and listening on {server_address}")

try:
    while True:
        # Receive data and address
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received {len(data)} bytes from {client_address}")
        print(f"Data: {data.decode('utf-8')}")
        
        # Send response
        message = f"Received: {data.decode('utf-8')}"
        server_socket.sendto(message.encode('utf-8'), client_address)
        print(f"Sent response to {client_address}")
        
except KeyboardInterrupt:
    print("Server is shutting down")
finally:
    server_socket.close()
```

### UDP Client

Here's a basic example of a UDP client:

```python
import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ('localhost', 10000)

try:
    # Send data
    message = "Hello, UDP server!"
    print(f"Sending: {message}")
    sent = client_socket.sendto(message.encode('utf-8'), server_address)
    
    # Receive response
    data, server = client_socket.recvfrom(1024)
    print(f"Received from {server}: {data.decode('utf-8')}")
    
finally:
    print("Closing socket")
    client_socket.close()
```

## UDP 소켓 프로그래밍

### UDP 서버

다음은 기본적인 UDP 서버의 예입니다:

```python
import socket

# UDP 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 소켓을 주소와 포트에 바인딩
server_address = ('localhost', 10000)
server_socket.bind(server_address)
print(f"UDP 서버가 {server_address}에서 실행 중이고 리스닝 중입니다")

try:
    while True:
        # 데이터와 주소 수신
        data, client_address = server_socket.recvfrom(1024)
        print(f"{client_address}에서 {len(data)} 바이트를 수신했습니다")
        print(f"데이터: {data.decode('utf-8')}")
        
        # 응답 전송
        message = f"수신: {data.decode('utf-8')}"
        server_socket.sendto(message.encode('utf-8'), client_address)
        print(f"{client_address}에 응답을 보냈습니다")
        
except KeyboardInterrupt:
    print("서버가 종료됩니다")
finally:
    server_socket.close()
```

### UDP 클라이언트

다음은 기본적인 UDP 클라이언트의 예입니다:

```python
import socket

# UDP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 서버 주소
server_address = ('localhost', 10000)

try:
    # 데이터 전송
    message = "안녕하세요, UDP 서버!"
    print(f"전송: {message}")
    sent = client_socket.sendto(message.encode('utf-8'), server_address)
    
    # 응답 수신
    data, server = client_socket.recvfrom(1024)
    print(f"{server}에서 수신: {data.decode('utf-8')}")
    
finally:
    print("소켓 닫는 중")
    client_socket.close()
```

## Socket Options and Timeouts

### Setting Socket Options

Socket options can be set to modify socket behavior:

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow reuse of local addresses
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Set buffer size
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 8192)
```

### Setting Timeouts

Setting timeouts prevents operations from blocking indefinitely:

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set timeout to 10 seconds
sock.settimeout(10.0)

try:
    # This will time out after 10 seconds if the connection fails
    sock.connect(('example.com', 80))
except socket.timeout:
    print("Connection timed out")
```

## 소켓 옵션 및 타임아웃

### 소켓 옵션 설정

소켓 옵션을 설정하여 소켓 동작을 수정할 수 있습니다:

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 로컬 주소 재사용 허용
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 버퍼 크기 설정
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 8192)
```

### 타임아웃 설정

타임아웃을 설정하면 작업이 무기한 차단되는 것을 방지할 수 있습니다:

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 타임아웃을 10초로 설정
sock.settimeout(10.0)

try:
    # 연결이 실패하면 10초 후에 타임아웃됩니다
    sock.connect(('example.com', 80))
except socket.timeout:
    print("연결 시간이 초과되었습니다")
```

## Handling Multiple Connections

For servers that need to handle multiple clients simultaneously, there are several approaches:

### Using `select`

The `select` module allows a program to monitor multiple sockets for events:

```python
import select
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('localhost', 10000))
server.listen(5)

inputs = [server]
outputs = []
message_queues = {}

while inputs:
    # Wait for at least one socket to be ready
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    # Handle readable sockets
    for s in readable:
        if s is server:
            # New connection
            client, client_address = s.accept()
            client.setblocking(0)
            inputs.append(client)
            message_queues[client] = []
        else:
            # Existing connection
            data = s.recv(1024)
            if data:
                message_queues[s].append(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                # Client disconnected
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]
    
    # Handle writable sockets
    for s in writable:
        if message_queues[s]:
            next_msg = message_queues[s][0]
            s.send(next_msg)
            message_queues[s] = message_queues[s][1:]
        else:
            outputs.remove(s)
    
    # Handle exceptional sockets
    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
```

### Using Threading

For simpler implementations, each client can be handled in a separate thread:

```python
import socket
import threading

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
            print(f"Received from {client_address}: {data.decode('utf-8')}")
            client_socket.sendall(f"Echo: {data.decode('utf-8')}".encode('utf-8'))
    finally:
        client_socket.close()
        print(f"Connection from {client_address} closed")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 10000))
    server.listen(5)
    print("Server is listening on localhost:10000")
    
    try:
        while True:
            client_socket, client_address = server.accept()
            
            # Create a new thread to handle the client
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down")
    finally:
        server.close()

if __name__ == "__main__":
    main()
```

## 다중 연결 처리

여러 클라이언트를 동시에 처리해야 하는 서버의 경우, 여러 접근 방식이 있습니다:

### `select` 사용

`select` 모듈을 사용하면 프로그램이 여러 소켓의 이벤트를 모니터링할 수 있습니다:

```python
import select
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('localhost', 10000))
server.listen(5)

inputs = [server]
outputs = []
message_queues = {}

while inputs:
    # 적어도 하나의 소켓이 준비될 때까지 대기
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    # 읽을 수 있는 소켓 처리
    for s in readable:
        if s is server:
            # 새 연결
            client, client_address = s.accept()
            client.setblocking(0)
            inputs.append(client)
            message_queues[client] = []
        else:
            # 기존 연결
            data = s.recv(1024)
            if data:
                message_queues[s].append(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                # 클라이언트 연결 해제
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]
    
    # 쓸 수 있는 소켓 처리
    for s in writable:
        if message_queues[s]:
            next_msg = message_queues[s][0]
            s.send(next_msg)
            message_queues[s] = message_queues[s][1:]
        else:
            outputs.remove(s)
    
    # 예외 소켓 처리
    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
```

### 스레딩 사용

더 간단한 구현을 위해, 각 클라이언트는 별도의 스레드에서 처리될 수 있습니다:

```python
import socket
import threading

def handle_client(client_socket, client_address):
    print(f"{client_address}에서 새 연결")
    
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
            print(f"{client_address}에서 수신: {data.decode('utf-8')}")
            client_socket.sendall(f"에코: {data.decode('utf-8')}".encode('utf-8'))
    finally:
        client_socket.close()
        print(f"{client_address}에서의 연결 닫힘")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 10000))
    server.listen(5)
    print("서버가 localhost:10000에서 리스닝 중입니다")
    
    try:
        while True:
            client_socket, client_address = server.accept()
            
            # 클라이언트를 처리할 새 스레드 생성
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()
    except KeyboardInterrupt:
        print("서버가 종료됩니다")
    finally:
        server.close()

if __name__ == "__main__":
    main()
```

## Non-blocking Sockets

Non-blocking sockets don't block when an operation can't be completed immediately:

```python
import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)  # Set to non-blocking mode

try:
    # This connect call will return immediately
    sock.connect(('example.com', 80))
except BlockingIOError:
    # Connection in progress
    pass

# Wait for connection to complete or timeout
ready = select.select([], [sock], [], 5.0)
if ready[1]:
    print("Connection established")
else:
    print("Connection timed out")
```

## 논블로킹 소켓

논블로킹 소켓은 작업을 즉시 완료할 수 없을 때 차단되지 않습니다:

```python
import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)  # 논블로킹 모드로 설정

try:
    # 이 connect 호출은 즉시 반환됩니다
    sock.connect(('example.com', 80))
except BlockingIOError:
    # 연결이 진행 중입니다
    pass

# 연결이 완료되거나 타임아웃될 때까지 대기
ready = select.select([], [sock], [], 5.0)
if ready[1]:
    print("연결이 설정되었습니다")
else:
    print("연결 시간이 초과되었습니다")
```

## Socket Server Framework

Python provides a `socketserver` module which simplifies the implementation of network servers:

```python
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the client socket
        data = self.request.recv(1024).strip()
        print(f"Received from {self.client_address[0]}: {data.decode('utf-8')}")
        
        # Send response
        response = f"Echo: {data.decode('utf-8')}"
        self.request.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 10000
    
    # Create the server, binding to localhost on port 10000
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        print(f"Server running on {HOST}:{PORT}")
        server.serve_forever()
```

For handling multiple connections:

```python
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        print(f"Received from {self.client_address[0]}: {data.decode('utf-8')}")
        response = f"Echo: {data.decode('utf-8')}"
        self.request.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 10000
    
    # ThreadingTCPServer uses a thread for each client
    with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f"Server running on {HOST}:{PORT}")
        server.serve_forever()
```

## 소켓 서버 프레임워크

Python은 네트워크 서버의 구현을 단순화하는 `socketserver` 모듈을 제공합니다:

```python
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request는 클라이언트 소켓입니다
        data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]}에서 수신: {data.decode('utf-8')}")
        
        # 응답 전송
        response = f"에코: {data.decode('utf-8')}"
        self.request.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 10000
    
    # 서버 생성, localhost의 10000번 포트에 바인딩
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # 서버 활성화; Ctrl-C로 프로그램을 중단할 때까지
        # 계속 실행됩니다
        print(f"서버가 {HOST}:{PORT}에서 실행 중입니다")
        server.serve_forever()
```

다중 연결 처리를 위해:

```python
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]}에서 수신: {data.decode('utf-8')}")
        response = f"에코: {data.decode('utf-8')}"
        self.request.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 10000
    
    # ThreadingTCPServer는 각 클라이언트에 대해 스레드를 사용합니다
    with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f"서버가 {HOST}:{PORT}에서 실행 중입니다")
        server.serve_forever()
```

## Best Practices

1. **Always close sockets**: Use `try...finally` blocks or context managers to ensure sockets are properly closed.

2. **Set timeouts**: Prevent operations from blocking indefinitely by setting appropriate timeouts.

3. **Error handling**: Properly catch and handle network-related exceptions.

4. **Buffer sizes**: Choose appropriate buffer sizes for your application's needs.

5. **Use non-blocking sockets or threads**: For handling multiple connections, use either non-blocking I/O with `select` or multi-threading approaches.

6. **Security**: Be cautious about accepting data from untrusted sources and validate all input.

## 모범 사례

1. **항상 소켓 닫기**: `try...finally` 블록이나 컨텍스트 매니저를 사용하여 소켓이 적절히 닫히도록 합니다.

2. **타임아웃 설정**: 적절한 타임아웃을 설정하여 작업이 무기한 차단되는 것을 방지합니다.

3. **오류 처리**: 네트워크 관련 예외를 적절하게 포착하고 처리합니다.

4. **버퍼 크기**: 애플리케이션의 요구에 맞는 적절한 버퍼 크기를 선택합니다.

5. **논블로킹 소켓이나 스레드 사용**: 다중 연결을 처리하기 위해 `select`를 사용한 논블로킹 I/O나 멀티스레딩 접근 방식을 사용합니다.

6. **보안**: 신뢰할 수 없는 소스에서 데이터를 받는 것에 주의하고 모든 입력을 검증합니다.

## Example: Simple Chat Server

Here's a more complete example implementing a simple chat server using threads:

```python
import socket
import threading

# List to keep track of all connected clients
clients = []
clients_lock = threading.Lock()

def broadcast(message, sender_socket=None):
    """Send message to all clients except the sender."""
    with clients_lock:
        for client in clients:
            # Don't send the message back to the sender
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    # Client probably disconnected
                    client.close()
                    clients.remove(client)

def handle_client(client_socket, client_address):
    """Handle a single client connection."""
    print(f"New connection from {client_address}")
    
    # Add the client to our list
    with clients_lock:
        clients.append(client_socket)
    
    # Send welcome message
    client_socket.send("Welcome to the chat server! Type 'quit' to exit.".encode('utf-8'))
    
    # Broadcast that a new user has joined
    broadcast(f"User from {client_address} has joined the chat.".encode('utf-8'), client_socket)
    
    try:
        while True:
            # Receive message from client
            data = client_socket.recv(1024)
            
            if not data:
                break
                
            message = data.decode('utf-8')
            
            # Check if the client wants to quit
            if message.strip().lower() == 'quit':
                break
                
            # Broadcast the message to all clients
            broadcast(f"User {client_address}: {message}".encode('utf-8'), client_socket)
            
    except:
        # Handle any unexpected errors
        pass
    finally:
        # Remove the client from our list and close the socket
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)
        
        client_socket.close()
        print(f"Connection from {client_address} closed")
        
        # Broadcast that the user has left
        broadcast(f"User from {client_address} has left the chat.".encode('utf-8'))

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind to all interfaces, port 8888
    server_address = ('', 8888)
    server.bind(server_address)
    
    # Listen for incoming connections (max 5 queued)
    server.listen(5)
    print("Chat server is running on port 8888")
    
    try:
        while True:
            # Accept a new connection
            client_socket, client_address = server.accept()
            
            # Start a new thread to handle the client
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        # Close the server socket
        server.close()

if __name__ == "__main__":
    main()
```

## 예제: 간단한 채팅 서버

다음은 스레드를 사용하여 간단한 채팅 서버를 구현한 보다 완전한 예입니다:

```python
import socket
import threading

# 모든 연결된 클라이언트를 추적하기 위한 리스트
clients = []
clients_lock = threading.Lock()

def broadcast(message, sender_socket=None):
    """발신자를 제외한 모든 클라이언트에게 메시지를 보냅니다."""
    with clients_lock:
        for client in clients:
            # 발신자에게 메시지를 다시 보내지 않습니다
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    # 클라이언트가 아마도 연결 해제되었습니다
                    client.close()
                    clients.remove(client)

def handle_client(client_socket, client_address):
    """단일 클라이언트 연결을 처리합니다."""
    print(f"{client_address}에서 새 연결")
    
    # 클라이언트를 리스트에 추가
    with clients_lock:
        clients.append(client_socket)
    
    # 환영 메시지 보내기
    client_socket.send("채팅 서버에 오신 것을 환영합니다! 종료하려면 'quit'를 입력하세요.".encode('utf-8'))
    
    # 새 사용자가 참여했음을 알림
    broadcast(f"{client_address}의 사용자가 채팅에 참여했습니다.".encode('utf-8'), client_socket)
    
    try:
        while True:
            # 클라이언트로부터 메시지 수신
            data = client_socket.recv(1024)
            
            if not data:
                break
                
            message = data.decode('utf-8')
            
            # 클라이언트가 종료하려는지 확인
            if message.strip().lower() == 'quit':
                break
                
            # 모든 클라이언트에게 메시지 전파
            broadcast(f"사용자 {client_address}: {message}".encode('utf-8'), client_socket)
            
    except:
        # 예상치 못한 오류 처리
        pass
    finally:
        # 리스트에서 클라이언트를 제거하고 소켓을 닫습니다
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)
        
        client_socket.close()
        print(f"{client_address}에서의 연결 닫힘")
        
        # 사용자가 나갔음을 알림
        broadcast(f"{client_address}의 사용자가 채팅에서 나갔습니다.".encode('utf-8'))

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 모든 인터페이스, 포트 8888에 바인딩
    server_address = ('', 8888)
    server.bind(server_address)
    
    # 들어오는 연결 대기(최대 5개 대기)
    server.listen(5)
    print("채팅 서버가 포트 8888에서 실행 중입니다")
    
    try:
        while True:
            # 새 연결 수락
            client_socket, client_address = server.accept()
            
            # 클라이언트를 처리할 새 스레드 시작
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("서버가 종료 중...")
    finally:
        # 서버 소켓 닫기
        server.close()

if __name__ == "__main__":
    main()
```

## Conclusion

Socket programming in Python provides a powerful way to create networked applications. With the `socket` module, you can implement everything from simple client-server applications to complex distributed systems.

This guide has covered the fundamentals of both TCP and UDP socket programming, handling multiple connections, non-blocking sockets, and best practices. By understanding these concepts, you can build robust and efficient networked applications in Python.

## 결론

Python에서의 소켓 프로그래밍은 네트워크 애플리케이션을 만드는 강력한 방법을 제공합니다. `socket` 모듈을 사용하면 간단한 클라이언트-서버 애플리케이션부터 복잡한 분산 시스템까지 모든 것을 구현할 수 있습니다.

이 가이드에서는 TCP 및 UDP 소켓 프로그래밍의 기본, 다중 연결 처리, 논블로킹 소켓 및 모범 사례를 다루었습니다. 이러한 개념을 이해함으로써 Python에서 강력하고 효율적인 네트워크 애플리케이션을 구축할 수 있습니다.

