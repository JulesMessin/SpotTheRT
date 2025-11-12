from threading import Thread
import socket

class ClientThread(Thread):
    def __init__(self, client_socket, client_address, client_username, controller):
        super().__init__()
        self.client_socket = client_socket
        self.client_address = client_address
        self.controller = controller
        self.client_username = client_username

    def run(self):
        print(f"Connexion : {self.client_address}")
        try:
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')

                self.controller.handle_message(self.client_address, self.client_username, message)
        except Exception as e:
            print(f"Erreur client {self.client_address}: {e}")
        finally:
            self.client_socket.close()
            self.controller.client_disconnected(self.client_address, self.client_username)