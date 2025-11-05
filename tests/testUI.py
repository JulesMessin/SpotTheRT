import sys
import socket
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget,
    QLineEdit, QPushButton, QLabel, QMessageBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal


# --- Thread de réception pour ne pas bloquer l'interface ---
class ReceptionThread(QThread):
    message_recu = pyqtSignal(str)

    def __init__(self, socket_client):
        super().__init__()
        self.socket_client = socket_client
        self.en_cours = True

    def run(self):
        while self.en_cours:
            try:
                data = self.socket_client.recv(1024)
                if data:
                    message = data.decode('utf-8')
                    self.message_recu.emit(message)
                else:
                    break
            except:
                break

    def stop(self):
        self.en_cours = False
        self.socket_client.close()


# --- Interface principale ---
class InterfaceClientSocket(QMainWindow):
    def __init__(self):
        super().__init__()
        self.socket_client = None
        self.thread_reception = None
        self.initialiserUI()

    def initialiserUI(self):
        self.setWindowTitle("Client TCP - PyQt5")
        self.setGeometry(200, 200, 600, 400)

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        layout = QVBoxLayout(widget_central)

        self.label_statut = QLabel("Statut : non connecté")
        layout.addWidget(self.label_statut)

        self.champ_ip = QLineEdit("127.0.0.1")
        self.champ_ip.setPlaceholderText("Adresse IP du serveur")
        layout.addWidget(self.champ_ip)

        self.champ_port = QLineEdit("55300")
        self.champ_port.setPlaceholderText("Port du serveur")
        layout.addWidget(self.champ_port)

        self.zone_texte = QTextEdit()
        self.zone_texte.setPlaceholderText("Entrez votre message ici...")
        layout.addWidget(self.zone_texte)

        self.bouton_connecter = QPushButton("Se connecter")
        self.bouton_connecter.clicked.connect(self.connecter_serveur)
        layout.addWidget(self.bouton_connecter)

        self.bouton_envoyer = QPushButton("Envoyer le message")
        self.bouton_envoyer.clicked.connect(self.envoyer_message)
        self.bouton_envoyer.setEnabled(False)
        layout.addWidget(self.bouton_envoyer)

        self.zone_reponse = QTextEdit()
        self.zone_reponse.setReadOnly(True)
        layout.addWidget(self.zone_reponse)

    # --- Connexion au serveur ---
    def connecter_serveur(self):
        ip = self.champ_ip.text()
        port = int(self.champ_port.text())

        try:
            self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_client.connect((ip, port))
            self.label_statut.setText(f"Connecté à {ip}:{port}")
            self.bouton_envoyer.setEnabled(True)

            # Démarrage du thread de réception
            self.thread_reception = ReceptionThread(self.socket_client)
            self.thread_reception.message_recu.connect(self.afficher_message)
            self.thread_reception.start()

        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Connexion échouée : {e}")
            self.label_statut.setText("Statut : erreur de connexion")

    # --- Envoi du message ---
    def envoyer_message(self):
        message = self.zone_texte.toPlainText().strip()
        if not message:
            return

        try:
            self.socket_client.send(message.encode('utf-8'))
            self.zone_texte.clear()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Échec d'envoi : {e}")

    # --- Réception du message du serveur ---
    def afficher_message(self, message):
        self.zone_reponse.append(f"Serveur : {message}")

    def closeEvent(self, event):
        if self.thread_reception:
            self.thread_reception.stop()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = InterfaceClientSocket()
    fenetre.show()
    sys.exit(app.exec_())
