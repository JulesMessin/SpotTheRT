import sys
import socket
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal


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


class SocketClientGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.client_socket = None
        self.receive_thread = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Client TCP - PyQt5")
        self.setGeometry(200, 200, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.status_label = QLabel("Statut : non connecté")
        layout.addWidget(self.status_label)

        self.ip_field = QLineEdit("127.0.0.1")
        self.ip_field.setPlaceholderText("Adresse IP du serveur")
        layout.addWidget(self.ip_field)

        self.port_field = QLineEdit("55300")
        self.port_field.setPlaceholderText("Port du serveur")
        layout.addWidget(self.port_field)

        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Entrez votre message ici...")
        layout.addWidget(self.message_input)

        self.connect_button = QPushButton("Se connecter")
        self.connect_button.clicked.connect(self.connect_to_server)
        layout.addWidget(self.connect_button)

        self.send_button = QPushButton("Envoyer le message")
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setEnabled(False)
        layout.addWidget(self.send_button)

        self.response_area = QTextEdit()
        self.response_area.setReadOnly(True)
        layout.addWidget(self.response_area)

    def connect_to_server(self):
        ip = self.ip_field.text()
        port = int(self.port_field.text())
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, port))
            self.status_label.setText(f"Connecté à {ip}:{port}")
            self.send_button.setEnabled(True)
            self.receive_thread = ReceiveThread(self.client_socket)
            self.receive_thread.message_received.connect(self.display_message)
            self.receive_thread.start()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Connexion échouée : {e}")
            self.status_label.setText("Statut : erreur de connexion")

    def send_message(self):
        message = self.message_input.toPlainText().strip()
        if not message:
            return
        try:
            self.client_socket.send(message.encode("utf-8"))
            self.message_input.clear()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Échec d'envoi : {e}")

    def display_message(self, message):
        self.response_area.append(f"Serveur : {message}")

    def closeEvent(self, event):
        if self.receive_thread:
            self.receive_thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SocketClientGUI()
    window.show()
    sys.exit(app.exec_())
