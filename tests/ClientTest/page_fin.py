import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class PageFin(QMainWindow):
    def __init__(self, gagnant="Anonyme"):
        super().__init__()
        self.setWindowTitle("Spot the RT - Fin de Partie")
        self.resize(500, 700)

        # --- CENTRAL WIDGET ---
        self.__blocprin = QWidget()
        self.__blocprin.setObjectName("MainBlock")
        self.__blocprin.setStyleSheet("""
            QWidget#MainBlock {
                border-image: url(pp.jpg) 0 0 0 0 stretch stretch;
            }
            QLabel { 
                color: white; 
                font-size: 15px; 
                font-weight: bold;
                background-color: #254758; 
                border: 2px solid #00d4ff;
                border-radius: 10px;
                padding: 15px;
            }
            QPushButton { 
                background-color: #254758; 
                color: white; 
                border: 2px solid #00d4ff;
                border-radius: 10px; 
                height: 50px; 
                font-weight: bold; 
                font-size: 14px;
            }
            QPushButton:hover { 
                background-color: #3e6e85; 
                border-color: #ffffff;
            }
        """)
        
        self.__blocprin_lay = QVBoxLayout()
        self.__blocprin.setLayout(self.__blocprin_lay)
        self.setCentralWidget(self.__blocprin)

        # --- TITRE DE FIN ---
        self.__titre = QLabel('PARTIE TERMINÉE')
        self.__titre.setAlignment(Qt.AlignCenter)
        self.__titre.setStyleSheet("""
            font-size: 30px; 
            color: #ffae00; 
            background-color: rgba(0, 0, 0, 180); 
            border: 3px solid #ffae00;
            margin-top: 50px;
        """)
        self.__blocprin_lay.addWidget(self.__titre)

        # --- AFFICHAGE DU GAGNANT ---
        self.__label_gagnant = QLabel(f"🏆 VAINQUEUR 🏆\n\n{gagnant.upper()}")
        self.__label_gagnant.setAlignment(Qt.AlignCenter)
        self.__label_gagnant.setStyleSheet("""
            font-size: 22px; 
            color: #00d4ff; 
            margin: 40px;
            border: 2px solid #00d4ff;
        """)
        self.__blocprin_lay.addWidget(self.__label_gagnant)

        self.__blocprin_lay.addStretch()

        # --- BOUTONS ---
        self.btn_rejouer = QPushButton('REJOUER')
        self.btn_rejouer.setStyleSheet("background-color: #2e7d32; border-color: #4caf50;") # Vert pour rejouer
        self.__blocprin_lay.addWidget(self.btn_rejouer)

        self.btn_quitter = QPushButton('QUITTER LE JEU')
        self.btn_quitter.setStyleSheet("background-color: #8b0000; border-color: #ff4444;")
        self.btn_quitter.clicked.connect(sys.exit)
        self.__blocprin_lay.addWidget(self.btn_quitter)