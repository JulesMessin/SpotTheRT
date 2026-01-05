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
                data = self.client_socket.recv(4096)
                if data:
                    message = data.decode("utf-8")
                    self.message_received.emit(message)
                else:
                    break
            except Exception:
                break

    def stop(self):
        self.running = False
        if self.client_socket:
            try:
                self.client_socket.close()
            except:
                pass

class ClientController:
    def __init__(self, model):
        self.model = model
        self.receive_thread = None

    def connect_to_server(self, ip, port, message_callback, username):
        """ Établit la connexion et lance le thread d'écoute """
        self.model.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.model.client_socket.settimeout(5) # Timeout de 5s pour la connexion
        self.model.client_socket.connect((ip, port))
        self.model.client_socket.settimeout(None) # On enlève le timeout pour la suite
        
        # Envoi du username dès la connexion (protocole simple)
        self.model.client_socket.send(username.encode("utf-8"))
        
        self.model.connected = True
        self.model.username = username

        # Lancement du thread d'écoute
        self.receive_thread = ReceiveThread(self.model.client_socket)
        self.receive_thread.message_received.connect(message_callback)
        self.receive_thread.start()

    def send_message(self, message):
        """ Envoie un message au serveur """
        if self.model.connected and self.model.client_socket:
            try:
                self.model.client_socket.send(message.encode("utf-8"))
            except Exception as e:
                print(f"Erreur d'envoi : {e}")

    def disconnect(self):
        """ Coupe proprement la connexion """
        if self.receive_thread:
            self.receive_thread.stop()
        self.model.connected = False