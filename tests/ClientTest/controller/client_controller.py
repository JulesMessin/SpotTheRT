from PyQt5.QtCore import QThread, pyqtSignal
import socket

class ReceiveThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket
        self.running = True

    def run(self):
        while self.running:
            try:
                data = self.client_socket.recv(1024)
                if data:
                    message = data.decode("utf-8")
                    self.message_received.emit(message)
                else:
                    break
            except Exception:
                break

    def stop(self):
        self.running = False
        self.client_socket.close()


class ClientController:
    def __init__(self, model):
        self.model = model
        self.receive_thread = None

    def connect_to_server(self, ip, port, message_callback, status_callback, username):
        try:
            self.model.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.model.client_socket.connect((ip, port))
            self.model.client_socket.send(username.encode("utf-8"))
            self.model.connected = True
            
            status_callback(f"Connecté à {ip}:{port} en tant que {username}")

            self.receive_thread = ReceiveThread(self.model.client_socket)
            self.receive_thread.message_received.connect(message_callback)
            self.receive_thread.start()
        except Exception as e:
            status_callback("Statut : erreur de connexion")
            raise e

    def send_message(self, message):
        if self.model.connected:
            try:
                self.model.client_socket.send(message.encode("utf-8"))
            except Exception as e:
                raise e

    def disconnect(self):
        if self.receive_thread:
            self.receive_thread.stop()
            self.model.connected = False
