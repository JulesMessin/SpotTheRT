from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QListWidget
from PyQt5.QtCore import Qt, pyqtSignal
from view.base_widgets import BackgroundWidget

class LobbyPage(QMainWindow):
    switch_to_game = pyqtSignal() # Signal pour aller en jeu

    def __init__(self, room_name, user_name, is_host):
        super().__init__()
        self.controller = None
        self.setWindowTitle("Lobby - Attente")
        self.resize(700, 800)
        self.is_host = is_host

        """ # --- Layout principal --- """
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.main_layout.setSpacing(40)

        """ #----------------------------------------------------------------# """

        """ -- Top Bar -- """
        self.top_bar = QHBoxLayout()
        self.btn_quit = QPushButton("Quitter")
        self.btn_quit.clicked.connect(self.close)
        self.top_bar.addStretch()
        self.top_bar.addWidget(self.btn_quit)
        self.main_layout.addLayout(self.top_bar)

        """ #----------------------------------------------------------------# """

        """ -- Titre -- """
        self.label_room = QLabel(f"SALLE : {room_name}")
        self.label_room.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.label_room.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.label_room)

        """ #----------------------------------------------------------------# """

        """ -- Liste Joueurs -- """
        self.label_p = QLabel("Joueurs connectés :")
        self.label_p.setStyleSheet("color: white;")
        self.list_players = QListWidget()
        self.list_players.addItem(f"{user_name} (Vous)")
        
        self.main_layout.addWidget(self.label_p)
        self.main_layout.addWidget(self.list_players)

        """ #----------------------------------------------------------------# """

        """ -- Actions -- """
        self.action_layout = QHBoxLayout()
        
        if self.is_host:
            self.btn_start = QPushButton("LANCER LA PARTIE")
            self.btn_start.setStyleSheet("background-color: #27ae60; color: white; font-weight: bold; padding: 10px;")
            self.btn_start.clicked.connect(self.on_start_clicked)
            self.action_layout.addStretch()
            self.action_layout.addWidget(self.btn_start)
            self.action_layout.addStretch()
        else:
            self.label_wait = QLabel("En attente de l'hôte...")
            self.label_wait.setStyleSheet("color: #f1c40f; font-size: 18px; font-style: italic;")
            self.label_wait.setAlignment(Qt.AlignCenter)
            self.action_layout.addWidget(self.label_wait)

        self.main_layout.addLayout(self.action_layout)

        """ #----------------------------------------------------------------# """

        self.central_widget = BackgroundWidget("pp.jpg")
        self.setCentralWidget(self.central_widget)
        self.content_widget = QWidget()
        self.content_widget.setLayout(self.main_layout)
        self.central_widget.layout.addWidget(self.content_widget, alignment=Qt.AlignCenter)

    def set_controller(self, controller):
        self.controller = controller

    def on_start_clicked(self):
        # L'hôte envoie le signal de départ au serveur
        if self.controller:
            self.controller.send_message("START_GAME")
            # Pour l'instant, on change aussi de page localement
            # Dans l'idéal, on attendrait que le serveur renvoie "GAME_START" à tout le monde
            self.switch_to_game.emit()