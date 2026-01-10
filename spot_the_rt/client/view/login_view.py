import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QGridLayout, 
                             QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt

from view.join_host_view import RoomDialog
from view.waiting_room_view import WaitingRoom


class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.setup_ui_bkiou()

    def setup_ui_fane(self):
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

        self.connect_button = QPushButton("Se connecter")
        layout.addWidget(self.connect_button)

    def setup_ui_bkiou(self):
        self.setWindowTitle("Spot the RT - Connexion")
        self.resize(500, 700)

        # --- STYLE CSS ---
        self.__blocprin = QWidget()
        self.__blocprin.setObjectName("MainBlock")
        self.__blocprin.setStyleSheet("""
            QWidget#MainBlock { border-image: url(spot_the_rt/client/pp.jpg) 0 0 0 0 stretch stretch; }
            QLabel { 
                color: white; font-size: 13px; font-weight: bold;
                background-color: #254758; border: 2px solid #00d4ff;
                border-radius: 5px; padding: 5px;
            }
            QLineEdit { 
                border: 2px solid #00d4ff; border-radius: 5px; 
                padding: 5px; background-color: white; color: black;
            }
            QPushButton { 
                background-color: #254758; color: white; border: 2px solid #00d4ff;
                border-radius: 10px; height: 45px; font-weight: bold; font-size: 14px;
            }
        """)
        
        layout = QVBoxLayout(self.__blocprin)
        self.setCentralWidget(self.__blocprin)

        # Titre
        self.__titre = QLabel('SPOT THE RT')
        self.__titre.setAlignment(Qt.AlignCenter)
        self.__titre.setStyleSheet("font-size: 35px; color: #00d4ff; background-color: rgba(0, 0, 0, 150); border: 3px solid #00d4ff; margin: 20px; padding: 10px;")
        layout.addWidget(self.__titre)

        # Status
        self.status_label = QLabel("Statut : non connecté")
        self.status_label.setStyleSheet("color: yellow; background-color: rgba(0,0,0,150);")
        layout.addWidget(self.status_label)

        # Champs
        grid = QGridLayout()
        self.ip_field = QLineEdit("127.0.0.1")
        self.port_field = QLineEdit("55305")
        self.username_field = QLineEdit()
        self.username_field.setPlaceholderText("Ton pseudo...")

        grid.addWidget(QLabel('IP SERVEUR'), 0, 0)
        grid.addWidget(self.ip_field, 0, 1)
        grid.addWidget(QLabel('PORT'), 1, 0)
        grid.addWidget(self.port_field, 1, 1)
        grid.addWidget(QLabel('PSEUDO'), 2, 0)
        grid.addWidget(self.username_field, 2, 1)
        
        layout.addLayout(grid)
        layout.addStretch()

        # Boutons
        self.connect_button = QPushButton('SE CONNECTER')
        layout.addWidget(self.connect_button)

        self.__btn_quitter = QPushButton('QUITTER LE JEU')
        self.__btn_quitter.setStyleSheet("background-color: #8b0000; border-color: #ff4444;")
        self.__btn_quitter.clicked.connect(self.close)
        layout.addWidget(self.__btn_quitter)

            
    def set_controller(self, controller):
        self.controller = controller
        self.connect_button.clicked.connect(self.on_connect)

    def on_connect(self):
        ip = self.ip_field.text()
        port = int(self.port_field.text())
        username = self.username_field.text()
        try:
            self.controller.connect_to_server(ip, port, self.display_message, self.update_status, username)
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


            room_name = dialog.room_name
            self.controller.send_message(f"server -room {room_name} -{mode}")


        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Connexion échouée : {e}")

    
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

