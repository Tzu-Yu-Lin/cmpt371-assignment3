# CMPT371 assignment3

## Project Description

This is a simple multi-client chat application built with Python socket programming. It uses TCP. The server accepts multiple client connections and broadcasts messages to all connected users. The client side includes a GUI made with Tkinter and a backend module for socket communication.

## Files

```text
server.py
client_gui.py
client_backend.py
```

## Requirements

* Python 3 installed
* Tkinter available in Python

## How to Run

### 1. Start the server

Open a terminal in the project folder and run:

```bash
python server.py
```

If `python` does not work, try:

```bash
python3 server.py
```

You should see something like:

```text
Server running on port 12345...
```

### 2. Start the first client

Open a second terminal in the same project folder and run:

```bash
python client_gui.py
```

If `python` does not work, try:

```bash
python3 client_gui.py
```

### 3. Connect the client

* Click the **Connect** button
* Enter a username
* Start sending messages

### 4. Connect more clients

Open more terminals and run:

```bash
python client_gui.py
```

## How the Program Works

* `server.py` creates the chat server and waits for client connections
* `client_backend.py` handles socket communication for the client
* `client_frontend.py` provides the gui

When a client connects, it sends a username to the server. After that, the client can send chat messages, and the server broadcasts them to other connected clients.

## Limitations

* No chat history is saved
* If the server is closed, all clients are disconnected
* The does not handle advanced features such as file transfer


## Possible Issues

* If the server is not started first, clients cannot connect
* If the port is already in use, the server may fail to start
* If Tkinter is not installed on a system, the GUI client may not open
* Closing the client window disconnects that user from the chat

