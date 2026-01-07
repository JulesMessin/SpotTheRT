from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QPushButton, QListWidget, QMessageBox
)
from PyQt5.QtCore import Qt

class WaitingRoom(QMainWindow):
    def __init__(self, username, room_name, is_host, parent=None):
        super().__init__()
        self.controller = None
        self.username = username
        self.room_name = room_name
        self.is_host = is_host
        self.players = [username]

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(f"Salle d'attente - {self.room_name}")
        self.setGeometry(250, 250, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.room_label = QLabel(f"Room : {self.room_name}")
        layout.addWidget(self.room_label)

        self.user_label = QLabel(f"Vous : {self.username} ({'Host' if self.is_host else 'Joueur'})")
        layout.addWidget(self.user_label)

        self.players_label = QLabel("Joueurs dans la room :")
        layout.addWidget(self.players_label)

        self.players_list = QListWidget()
        self.players_list.addItems(self.players)
        layout.addWidget(self.players_list)

        self.start_button = QPushButton("Démarrer la partie")
        layout.addWidget(self.start_button)

        self.quit_button = QPushButton("Quitter la room")
        layout.addWidget(self.quit_button)


    def set_controller(self, controller):
        self.controller = controller
        self.quit_button.clicked.connect(lambda: self.controller.leave_waiting_room(self.room_name))
        
        self.start_button.clicked.connect(lambda: self.controller.launch_game(self.room_name))
        self.start_button.clicked.connect(lambda: print("envoyé"))



       