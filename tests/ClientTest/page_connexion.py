import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QGridLayout, QLabel, QLineEdit, QPushButton, 
                             QCheckBox, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt



###
from page_salle import SalleAttente
###



class SpotTheRT(QMainWindow):
    TITRE_FENETRE = "Spot the RT - Connexion"

    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.TITRE_FENETRE)
        self.resize(500, 700)
        
        # --- CENTRAL WIDGET ---
        self.__blocprin = QWidget()
        self.__blocprin.setObjectName("MainBlock")
        self.__blocprin.setStyleSheet("""
            QWidget#MainBlock {
                border-image: url(pp.jpg) 0 0 0 0 stretch stretch;
            }
            
            /* Style des Labels avec fond et bordures */
            QLabel { 
                color: white; 
                font-size: 13px; 
                font-weight: bold;
                background-color: #254758; 
                border: 2px solid #00d4ff;
                border-radius: 5px;
                padding: 5px;
            }

            /* Style des Champs de saisie */
            QLineEdit { 
                border: 2px solid #00d4ff;
                border-radius: 5px; 
                padding: 5px; 
                background-color: white;
                color: black;
                selection-background-color: #00d4ff;
            }

            /* Style des Boutons */
            QPushButton { 
                background-color: #254758; 
                color: white; 
                border: 2px solid #00d4ff;
                border-radius: 10px; 
                height: 45px; 
                font-weight: bold; 
                font-size: 14px;
            }
            
            /* Case à cocher */
            QCheckBox { 
                color: white; 
                font-weight: bold; 
                background-color: rgba(37, 71, 88, 180); 
                padding: 5px;
                border-radius: 5px;
            }
        """)
        
        self.__blocprin_lay = QVBoxLayout()
        self.__blocprin.setLayout(self.__blocprin_lay)
        self.setCentralWidget(self.__blocprin)

        # --- TITRE ---
        self.__titre_jeu = QLabel('SPOT THE RT')
        self.__titre_jeu.setAlignment(Qt.AlignCenter)
        self.__titre_jeu.setStyleSheet("""
            font-size: 35px; 
            color: #00d4ff; 
            background-color: rgba(0, 0, 0, 150); 
            border: 3px solid #00d4ff;
            margin: 20px;
            padding: 10px;
        """)
        self.__blocprin_lay.addWidget(self.__titre_jeu)

        # --- CHAMPS --
        self.__bloc_champs = QWidget()
        self.__grille = QGridLayout()
        self.__bloc_champs.setLayout(self.__grille)

        # Création des éléments
        self.__input_ip = QLineEdit()
        self.__input_ip.setPlaceholderText("ex: 192.168.1.1")
        
        self.__input_salle = QLineEdit()
        self.__input_salle.setPlaceholderText("Nom du salon")

        self.__input_pseudo = QLineEdit()
        self.__input_pseudo.setPlaceholderText("Ton pseudo")

        self.__check_host = QCheckBox("Devenir l'hôte de la partie")

        # Positionnement dans la grille 
        self.__grille.addWidget(QLabel('IP SERVEUR'), 0, 0)
        self.__grille.addWidget(self.__input_ip, 0, 1)
        
        self.__grille.addWidget(QLabel('NOM SALLE'), 1, 0)
        self.__grille.addWidget(self.__input_salle, 1, 1)

        self.__grille.addWidget(QLabel('PSEUDO'), 2, 0)
        self.__grille.addWidget(self.__input_pseudo, 2, 1)

        self.__grille.addWidget(self.__check_host, 3, 0, 1, 2)

        self.__blocprin_lay.addWidget(self.__bloc_champs)
        
        # Espace pour pousser les boutons vers le bas
        self.__blocprin_lay.addStretch()

        # --- BOUTONS ---
        self.__btn_valider = QPushButton('VALIDER LA CONNEXION')
        self.__btn_valider.clicked.connect(self.fct_valider)
        self.__blocprin_lay.addWidget(self.__btn_valider)

        self.__btn_reset = QPushButton('EFFACER LES CHAMPS')
        self.__btn_reset.setStyleSheet("background-color: #444; border-color: #888;")
        self.__btn_reset.clicked.connect(self.fct_reset)
        self.__blocprin_lay.addWidget(self.__btn_reset)

        self.__btn_quitter = QPushButton('QUITTER LE JEU')
        self.__btn_quitter.setStyleSheet("background-color: #8b0000; border-color: #ff4444;")
        self.__btn_quitter.clicked.connect(self.fct_quitter)
        self.__blocprin_lay.addWidget(self.__btn_quitter)




    # --- MÉTHODES ---
    def fct_quitter(self):
        sys.exit()

    def fct_reset(self):
        self.__input_ip.clear()
        self.__input_salle.clear()
        self.__input_pseudo.clear()
        self.__check_host.setChecked(False)

    def fct_valider(self):

        pseudo = self.__input_pseudo.text()
        salle = self.__input_salle.text()
        ip = self.__input_ip.text()
        est_host = self.__check_host.isChecked()

        if not pseudo or not salle or not ip:
            QMessageBox.critical(self, "Erreur", "Tous les champs doivent être remplis !")
        else:
            self.page_salle = SalleAttente(pseudo, salle, est_host)
            self.page_salle.show()
            self.hide() 
     
       #        ^
       #        |
       #        |
        ### --- "Pour mon camarade qui veut continuer pour rediriger vers un controller c'est la que ca ce passe vos grand mere" ----



