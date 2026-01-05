import socket

class ClientModel:
    def __init__(self):
        self.client_socket = None
        self.connected = False
        self.username = ""
        self.room_name = ""
        self.is_host = False