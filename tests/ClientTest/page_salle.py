import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer, QTime


### la ligne la elle est a enlever de ce module la, c'est juste pour tester l'affichage
### elle sera a mettre dans le controller
#             |
#             |
#             v
from page_fin import PageFin

from page_jeu import PageJeu



class SalleAttente(QMainWindow):
    def __init__(self, pseudo, salle, est_host=False):
        super().__init__()
        self.setWindowTitle("Spot the RT - Salle d'Attente")
        self.resize(500, 700)
        self.est_host = est_host

        self.__blocprin = QWidget()
        self.__blocprin.setObjectName("MainBlock")
        self.__blocprin.setStyleSheet("""
            QWidget#MainBlock { border-image: url(pp.jpg) 0 0 0 0 stretch stretch; }
            QLabel { color: white; font-size: 13px; font-weight: bold; background-color: #254758; border: 2px solid #00d4ff; border-radius: 5px; padding: 10px; }
            QPushButton { background-color: #254758; color: white; border: 2px solid #00d4ff; border-radius: 10px; height: 45px; font-weight: bold; }
            QPushButton:hover { background-color: #3e6e85; }
        """)
        
        layout = QVBoxLayout()
        self.__blocprin.setLayout(layout)
        self.setCentralWidget(self.__blocprin)

       
        self.__titre = QLabel(f"SALLE : {salle.upper()}")
        self.__titre.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.__titre)

        self.__label_timer = QLabel("Temps d'attente : 00:00")
        self.__label_timer.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.__label_timer)

        self.__temps = QTime(0, 0)
        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.timer)
        self.__timer.start(1000)

        layout.addStretch()


        # --- BOUTONS ---
        if self.est_host:
            self.btn_lancer = QPushButton('LANCER LA PARTIE')
            self.btn_lancer.setStyleSheet("background-color: #006400; border-color: #00ff00;")
            self.btn_lancer.clicked.connect(self.lancerlagame)
            layout.addWidget(self.btn_lancer)

        self.btn_quitter = QPushButton('QUITTER LA SALLE')
        self.btn_quitter.setStyleSheet("background-color: #8b0000; border-color: #ff4444;")
        self.btn_quitter.clicked.connect(self.close)
        layout.addWidget(self.btn_quitter)



    # --- MÉTHODES ---
    def timer(self):
        self.__temps = self.__temps.addSecs(1)
        self.__label_timer.setText(f"Temps d'attente : {self.__temps.toString('mm:ss')}")

    def lancerlagame(self):

        self.ecran_jeu = PageJeu()
        self.ecran_jeu.show()

        '''
        ### ca c'est cencer etre une fonction dans le controller 
        nom_vainqueur = self.modele.get_winner_name()
        self.ecran_fin = PageFin(nom_vainqueur)
        self.ecran_fin.show()
        ###
     '''