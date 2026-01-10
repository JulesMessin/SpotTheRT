from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel, 
                             QPushButton, QListWidget, QMessageBox)
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QMessageBox



class WaitingRoom(QMainWindow):
    def __init__(self, username, room_name, is_host, parent=None):
        super().__init__()
        self.controller = None
        self.username = username
        self.room_name = room_name
        self.is_host = is_host
        self.players = [username]

        self.setup_ui_bkiou()

    def setup_ui_fane(self):
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

    def setup_ui_bkiou(self):
        self.setWindowTitle(f"Spot the RT - Salle : {self.room_name}")
        self.resize(500, 700)

        self.__blocprin = QWidget()
        self.__blocprin.setObjectName("MainBlock")
        self.__blocprin.setStyleSheet("""
            QWidget#MainBlock { border-image: url(spot_the_rt/client/pp.jpg) 0 0 0 0 stretch stretch; }
            QLabel { color: white; font-size: 13px; font-weight: bold; background-color: #254758; border: 2px solid #00d4ff; border-radius: 5px; padding: 10px; }
            QListWidget { background-color: rgba(37, 71, 88, 200); color: white; border: 2px solid #00d4ff; font-weight: bold; }
            QPushButton { background-color: #254758; color: white; border: 2px solid #00d4ff; border-radius: 10px; height: 45px; font-weight: bold; }
        """)
        
        layout = QVBoxLayout(self.__blocprin)
        self.setCentralWidget(self.__blocprin)

        # Titre de la salle
        self.room_label = QLabel(f"SALLE : {self.room_name.upper()}")
        self.room_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.room_label)

        # Timer
        self.__label_timer = QLabel("Temps d'attente : 00:00")
        self.__label_timer.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.__label_timer)

        self.__temps = QTime(0, 0)
        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.update_timer)
        self.__timer.start(1000)

        # Liste des joueurs
        layout.addWidget(QLabel("JOUEURS CONNECTÉS :"))
        self.players_list = QListWidget()
        self.players_list.addItems(self.players)
        layout.addWidget(self.players_list)

        layout.addStretch()

        # Boutons
        if self.is_host:
            self.rounds_label = QLabel("NOMBRE DE ROUNDS :")
            self.rounds_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(self.rounds_label)

            self.rounds_spinbox = QSpinBox()
            self.rounds_spinbox.setMinimum(1)
            self.rounds_spinbox.setMaximum(20)
            self.rounds_spinbox.setValue(5)
            self.rounds_spinbox.setAlignment(Qt.AlignCenter)
            self.rounds_spinbox.setStyleSheet("""
                QSpinBox {
                    background-color: #254758;
                    color: white;
                    border: 2px solid #00d4ff;
                    font-weight: bold;
                    height: 35px;
                }
            """)
            layout.addWidget(self.rounds_spinbox)


            self.start_button = QPushButton('LANCER LA PARTIE')
            self.start_button.setStyleSheet("background-color: #006400; border-color: #00ff00;")
            layout.addWidget(self.start_button)

        self.quit_button = QPushButton('QUITTER LA SALLE')
        self.quit_button.setStyleSheet("background-color: #8b0000; border-color: #ff4444;")
        layout.addWidget(self.quit_button)

    """
    def set_controller(self, controller):
        self.controller = controller
        self.quit_button.clicked.connect(lambda: self.controller.leave_waiting_room(self.room_name))
        
        self.start_button.clicked.connect(lambda: self.controller.launch_game(self.room_name))
        self.start_button.clicked.connect(lambda: print("envoyé"))
    """

    def set_controller(self, controller):
        self.controller = controller
        self.quit_button.clicked.connect(lambda: self.controller.leave_waiting_room(self.room_name))
        if self.is_host:
            self.start_button.clicked.connect(self.on_launch_clicked)

    def update_timer(self):
        self.__temps = self.__temps.addSecs(1)
        self.__label_timer.setText(f"Temps d'attente : {self.__temps.toString('mm:ss')}")

    def update_player_list(self, new_players):
        """ Appelée par le controller pour rafraîchir la liste """
        self.players_list.clear()
        self.players_list.addItems(new_players)


    def on_launch_clicked(self):
        nb_round = self.rounds_spinbox.value()
        self.controller.launch_game(self.room_name, nb_round)
