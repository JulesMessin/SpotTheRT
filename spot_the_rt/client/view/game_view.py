from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,QTextEdit, 
    QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QFrame)

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

class GameView(QMainWindow):
    def __init__(self, username, room_name):
        super().__init__()
        self.username = username
        self.room_name = room_name
        self.controller = None

        self.setup_ui2()

    def setup_ui(self):
        self.setWindowTitle(f"Jeu - {self.room_name}")
        self.setGeometry(200, 200, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.info_label = QLabel(f"{self.username} dans la room '{self.room_name}'")
        layout.addWidget(self.info_label)

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        layout.addWidget(self.chat_area)

        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Entrez votre message ici...")
        layout.addWidget(self.message_input)

        self.send_button = QPushButton("Envoyer le message")
        layout.addWidget(self.send_button)

        self.quit_button = QPushButton("Quitter la partie")
        layout.addWidget(self.quit_button)
    
    def setup_ui2(self):
        self.setWindowTitle("Spot the RT - EN JEU")
        self.resize(850, 650) 

        # --- STYLE GLOBAL ---
        self.__central_widget = QWidget()
        self.__central_widget.setObjectName("MainBlock")
        self.__central_widget.setStyleSheet("""
            QWidget#MainBlock {
                border-image: url(pp.jpg) 0 0 0 0 stretch stretch;
            }
            QLabel {
                color: white; font-weight: bold; font-size: 16px;
                background-color: rgba(37, 71, 88, 200);
                border: 2px solid #00d4ff; border-radius: 5px; padding: 5px;
            }
            /* Style des boutons de jeu (Symboles) */
            QPushButton {
                background-color: white;
                border: 2px solid #254758;
                border-radius: 12px; /* Un peu plus arrondi */
                margin: 5px; /* Espacement entre les boutons */
            }
            QPushButton:hover {
                background-color: #e0f7fa;
                border-color: #00d4ff;
            }
            /* Ligne de séparation */
            QFrame#Separateur {
                background-color: #00d4ff;
                width: 3px;
            }
            /* Conteneur des grilles pour l'aspect "rond" (Optionnel) */
            QWidget#ConteneurCarte {
                background-color: rgba(255, 255, 255, 0.1);
                border: 3px solid #00d4ff;
                border-radius: 150px; /* Donne l'aspect circulaire au conteneur global */
                padding: 20px;
            }
        """)
        
        self.main_layout = QVBoxLayout()
        self.__central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.__central_widget)

        #central_widget = QWidget()
        #self.setCentralWidget(central_widget)
        #layout = QVBoxLayout(central_widget)


        self.barre_info = QHBoxLayout()
        self.label_round = QLabel("ROUND : 1 / 5")
        self.label_round.setAlignment(Qt.AlignCenter)
        self.label_score = QLabel("SCORE : 0 PTS")
        self.label_score.setAlignment(Qt.AlignCenter)
        self.label_score.setStyleSheet("color: #ffae00; border-color: #ffae00;")
        self.barre_info.addWidget(self.label_round)
        self.barre_info.addStretch()
        self.barre_info.addWidget(self.label_score)
        self.main_layout.addLayout(self.barre_info)


        self.zone_cartes = QHBoxLayout()
        
        # --- CARTE  ---
        self.layout_cible = QVBoxLayout()
        self.titre_cible = QLabel("CARTE À TROUVER")
        self.titre_cible.setAlignment(Qt.AlignCenter)
        self.layout_cible.addWidget(self.titre_cible)

        self.grid_cible = QGridLayout()
        self.liste_btn_cible = [] 
        self._generer_grille_3x3(self.grid_cible, self.liste_btn_cible, est_joueur=False)
        
        # On met la grille dans un conteneur pour essayer de lui donner une forme
        container_cible = QWidget()
        container_cible.setObjectName("ConteneurCarte")
        container_cible.setLayout(self.grid_cible)
        self.layout_cible.addWidget(container_cible)

        # --- SÉPARATEUR ---
        self.separateur = QFrame()
        self.separateur.setObjectName("Separateur")
        self.separateur.setFrameShape(QFrame.VLine)
        
        # --- CARTE JOUEUR ---
        self.layout_joueur = QVBoxLayout()
        self.titre_joueur = QLabel("TA CARTE")
        self.titre_joueur.setAlignment(Qt.AlignCenter)
        self.titre_joueur.setStyleSheet("border-color: #00ff00; color: #00ff00;")
        self.layout_joueur.addWidget(self.titre_joueur)

        self.grid_joueur = QGridLayout()
        self.liste_btn_joueur = [] 
        self._generer_grille_3x3(self.grid_joueur, self.liste_btn_joueur, est_joueur=True)

        container_joueur = QWidget()
        container_joueur.setObjectName("ConteneurCarte") 
        container_joueur.setLayout(self.grid_joueur)
        self.layout_joueur.addWidget(container_joueur)

        # Ajout au layout principal
        self.zone_cartes.addLayout(self.layout_cible)
        self.zone_cartes.addWidget(self.separateur)
        self.zone_cartes.addLayout(self.layout_joueur)
        
        self.main_layout.addLayout(self.zone_cartes)

        # Ajout de la zone de chat
        self.info_label = QLabel(f"{self.username} dans la room '{self.room_name}'")
        self.main_layout.addWidget(self.info_label)

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.main_layout.addWidget(self.chat_area)

        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Entrez votre message ici...")
        self.main_layout.addWidget(self.message_input)

        self.send_button = QPushButton("Envoyer le message")
        self.main_layout.addWidget(self.send_button)

        self.quit_button = QPushButton("Quitter la partie")
        self.main_layout.addWidget(self.quit_button)


    def _generer_grille_3x3(self, grille, liste_stockage, est_joueur):

        btn_index = 0 # 
        

        for row in range(3):
            for col in range(3):

                if row == 1 and col == 1:
                    continue
                

                btn = QPushButton()
 
                btn.setFixedSize(75, 75) 
                btn.setIconSize(QSize(55, 55))
                
                if est_joueur:

                    btn.clicked.connect(lambda checked, idx=btn_index: self.clic_carte_joueur(idx))
                else:
                    btn.setEnabled(False) 
                    btn.setStyleSheet("background-color: #ddd; border: 2px solid #555; margin: 5px;")


                grille.addWidget(btn, row, col)
                liste_stockage.append(btn)
                btn_index += 1

   
    def update_score_round(self, score, num_round):
        self.label_score.setText(f"SCORE : {score} PTS")
        self.label_round.setText(f"ROUND : {num_round}")

    def update_images(self, noms_img_cible, noms_img_joueur):
        for i, nom in enumerate(noms_img_cible):
            if i < len(self.liste_btn_cible):
                self.liste_btn_cible[i].setIcon(QIcon(nom)) 
        
        for i, nom in enumerate(noms_img_joueur):
            if i < len(self.liste_btn_joueur):
                self.liste_btn_joueur[i].setIcon(QIcon(nom))

    def clic_carte_joueur(self, index_bouton):
        print(f"Bouton {index_bouton} cliqué !") 




    def set_controller(self, controller):
        self.controller = controller

        self.send_button.clicked.connect(self.on_send)

        self.quit_button.clicked.connect(lambda: self.controller.leave_game(self.room_name))

    def on_send(self):
        message = self.message_input.toPlainText().strip()
        if message and self.controller:
            self.controller.send_message(f"server -room {self.room_name} -chat {message}")
            self.message_input.clear()
        print("envoyé")


    def display_message(self, message):
        self.chat_area.append(message)
