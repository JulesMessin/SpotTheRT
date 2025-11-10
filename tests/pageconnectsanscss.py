import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QPushButton, QWidget, QLineEdit, QLabel, QCheckBox
)
from PyQt5.QtCore import Qt


class Spot_the_rt(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spot the rt")
        self.resize(700, 800)

        # --- Layout principal vertical ---
        self.main_layout = QVBoxLayout()

        # --- Top layout ---
        self.top_layout = QHBoxLayout()


        self.button_reset = QPushButton("Reset")
        self.button_reset.clicked.connect(self.reset_form)
        self.top_layout.addWidget(self.button_reset)  

        self.top_layout.addStretch()


        self.button_fermer = QPushButton("Fermer")
        self.button_fermer.clicked.connect(self.close)
        self.top_layout.addWidget(self.button_fermer)

        self.main_layout.addLayout(self.top_layout)

        # --- ADRESSE IP SERVEUR ---
        self.ip_layout = QHBoxLayout()
        self.ip_layout.addStretch()
        self.label_ip_server = QLabel("Adresse IP du serveur :")
        self.ip_addr = QLineEdit()
        self.ip_addr.setAlignment(Qt.AlignCenter)
        self.ip_layout.addWidget(self.label_ip_server)
        self.ip_layout.addWidget(self.ip_addr)
        self.ip_layout.addStretch()
        self.main_layout.addLayout(self.ip_layout)

        # --- NOM DE LA SALLE ---
        self.salle_layout = QHBoxLayout()
        self.salle_layout.addStretch()
        self.label_salle = QLabel("Nom de la salle :")
        self.line_salle = QLineEdit()
        self.salle_layout.addWidget(self.label_salle)
        self.salle_layout.addWidget(self.line_salle)
        self.salle_layout.addStretch()
        self.main_layout.addLayout(self.salle_layout)

        # --- CASE À COCHER HÔTE ---
        self.host_layout = QHBoxLayout()
        self.host_layout.addStretch()
        self.checkbox_host = QCheckBox("Hôte")
        self.host_layout.addWidget(self.checkbox_host)
        self.host_layout.addStretch()
        self.main_layout.addLayout(self.host_layout)

        # --- NOM UTILISATEUR ---
        self.user_layout = QHBoxLayout()
        self.user_layout.addStretch()
        self.label_user = QLabel("Nom d’utilisateur :")
        self.line_user = QLineEdit()
        self.user_layout.addWidget(self.label_user)
        self.user_layout.addWidget(self.line_user)
        self.user_layout.addStretch()
        self.main_layout.addLayout(self.user_layout)



        # --- Définir le widget central ---
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        
        # --- Bouton valider centre ---
        self.bottomlayout = QHBoxLayout()
        self.button_valider = QPushButton("Valider")
        self.button_fermer.clicked.connect(self.Valider)
        self.bottomlayout.addStretch()
        self.bottomlayout.addWidget(self.button_valider)

        self.bottomlayout.addStretch()
        self.main_layout.addLayout(self.bottomlayout)
        
        
    def reset_form(self):
        self.ip_addr.clear()
        self.line_salle.clear()
        self.line_user.clear()
        self.checkbox_host.setChecked(False)
    def Valider(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = Spot_the_rt()
    fen.show()
    sys.exit(app.exec())

