import socket


class SocketClient:
    def __init__(self):
        self.client = socket.socket()
        self.client.connect(
            ('127.0.0.1', 9527)
        )

    def get_client(self):
        return self.client

# sk = SocketClient()
# client = sk.get_client()