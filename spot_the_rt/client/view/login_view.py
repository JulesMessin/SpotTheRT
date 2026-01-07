from view.join_host_view import RoomDialog



from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QTextEdit, QPushButton, QMessageBox, QDialog
)


class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = None
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

        self.port_field = QLineEdit("55305")
        self.port_field.setPlaceholderText("Port du serveur")
        layout.addWidget(self.port_field)

        self.username_field = QLineEdit("")
        self.username_field.setPlaceholderText("Username")
        layout.addWidget(self.username_field)

        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Entrez votre message ici...")
        layout.addWidget(self.message_input)

        self.connect_button = QPushButton("Se connecter")
        layout.addWidget(self.connect_button)

        self.send_button = QPushButton("Envoyer le message")
        self.send_button.setEnabled(False)
        layout.addWidget(self.send_button)

        self.response_area = QTextEdit()
        self.response_area.setReadOnly(True)
        layout.addWidget(self.response_area)

            
    def set_controller(self, controller):
        self.controller = controller
        self.connect_button.clicked.connect(self.on_connect)
        self.send_button.clicked.connect(self.on_send)

    def on_connect(self):
        ip = self.ip_field.text()
        port = int(self.port_field.text())
        username = self.username_field.text()
        try:
            self.controller.connect_to_server(ip, port, self.display_message, self.update_status, username)
            self.send_button.setEnabled(True)
            #

            msg = QMessageBox(self)
            msg.setWindowTitle("Room")
            host_btn = msg.addButton("Host", QMessageBox.AcceptRole)
            join_btn = msg.addButton("Join", QMessageBox.RejectRole)
            msg.exec_()

            mode = "host" if msg.clickedButton() == host_btn else "join"

            dialog = RoomDialog(mode, self)
            if not dialog.exec_(): 
                return


            room = dialog.room_name
            self.controller.send_message(f"game -room {room} -{mode}")


        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Connexion échouée : {e}")



    def on_send(self):
        message = self.message_input.toPlainText().strip()
        if message:
            try:
                self.controller.send_message(message)
                self.message_input.clear()
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Échec d'envoi : {e}")
    
    def display_message(self, message):
        self.response_area.append(message)

    def update_status(self, status):
        self.status_label.setText(status)

    def closeEvent(self, event):
        if self.controller:
            self.controller.disconnect()
        event.accept()

    ## popup host/ join

    def show_host_join_popup(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Salle")
        msg.setText("Souhaitez-vous host ou rejoindre une room ?")
        msg.setIcon(QMessageBox.Question)

        host_btn = msg.addButton("Host la room", QMessageBox.AcceptRole)
        join_btn = msg.addButton("Join une room", QMessageBox.RejectRole)

        msg.exec_()

        if msg.clickedButton() == host_btn:
            return "host"
        elif msg.clickedButton() == join_btn:
            return "join"
        return None

