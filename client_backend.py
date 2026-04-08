import socket
import threading


class CBackend:
    def __init__(self, host, port, msg, disc):
        self.host = host
        self.port = port
        self.msg = msg
        self.disc = disc
        self.client = None
        self.running = False

    def join(self, username):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.client.sendall(username.encode())
        self.running = True
        threading.Thread(target=self.recv, daemon=True).start()

    def recv(self):
        while self.running:
            data = self.client.recv(20000).decode()
            if not data:
                break
            self.msg(data)
        self.running = False
        self.disc()

    def send(self, text):
        if self.client:
            self.client.sendall(text.encode())

    def close(self):
        self.running = False
        if self.client:
            self.client.close()
            self.client = None