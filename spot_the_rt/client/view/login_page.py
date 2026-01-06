from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QLabel, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from view.base_widgets import BackgroundWidget

class LoginPage(QMainWindow):
    # Signal émis quand la connexion est réussie (Room, User, IsHost)
    switch_to_lobby = pyqtSignal(str, str, bool)

    def __init__(self):
        super().__init__()
        self.controller = None
        self.setWindowTitle("Spot the RT - Connexion")
        self.resize(700, 800)

        """ # --- Layout principal vertical --- """
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.main_layout.setSpacing(60)

        """ #----------------------------------------------------------------# """

        """ -- Top layout -- """
        self.top_layout = QHBoxLayout()
        self.button_reset = QPushButton("Reset")
        self.button_reset.clicked.connect(self.func_reset)
        self.button_quitter = QPushButton("Quitter")
        self.button_quitter.clicked.connect(self.close)
        
        self.top_layout.addWidget(self.button_reset)
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.button_quitter)
        self.main_layout.addLayout(self.top_layout)

        """ #----------------------------------------------------------------# """

        """ -- Ip layout -- """
        self.ip_layout = QHBoxLayout()
        self.label_ip = QLabel("IP Serveur :")
        self.ip_addr = QLineEdit("127.0.0.1")
        self.ip_addr.setAlignment(Qt.AlignCenter)
        self.ip_layout.addWidget(self.label_ip)
        self.ip_layout.addWidget(self.ip_addr)
        self.main_layout.addLayout(self.ip_layout)

        """ #----------------------------------------------------------------# """

        """ -- Salle layout -- """
        self.salle_layout = QHBoxLayout()
        self.line_salle = QLineEdit()
        self.line_salle.setPlaceholderText("Nom de la salle")
        self.line_salle.setAlignment(Qt.AlignCenter)
        self.salle_layout.addWidget(QLabel("Salle :"))
        self.salle_layout.addWidget(self.line_salle)
        self.main_layout.addLayout(self.salle_layout)

        """ #----------------------------------------------------------------# """

        """ -- Host layout -- """
        self.host_layout = QHBoxLayout()
        self.checkbox_host = QCheckBox("Hôte (Créer la partie)")
        self.host_layout.addStretch()
        self.host_layout.addWidget(self.checkbox_host)
        self.host_layout.addStretch()
        self.main_layout.addLayout(self.host_layout)

        """ #----------------------------------------------------------------# """

        """ -- User layout -- """
        self.user_layout = QHBoxLayout()
        self.line_user = QLineEdit()
        self.line_user.setPlaceholderText("Votre Pseudo")
        self.line_user.setAlignment(Qt.AlignCenter)
        self.user_layout.addWidget(QLabel("Pseudo :"))
        self.user_layout.addWidget(self.line_user)
        self.main_layout.addLayout(self.user_layout)

        """ #----------------------------------------------------------------# """

        """ -- Bottom layout -- """
        self.bottom_layout = QHBoxLayout()
        self.button_valider = QPushButton("VALIDER")
        self.button_valider.clicked.connect(self.on_validate)
        self.bottom_layout.addStretch()
        self.bottom_layout.addWidget(self.button_valider)
        self.bottom_layout.addStretch()
        self.main_layout.addLayout(self.bottom_layout)

        """ #----------------------------------------------------------------# """

        self.central_widget = BackgroundWidget("pp.jpg")
        self.setCentralWidget(self.central_widget)
        self.content_widget = QWidget()
        self.content_widget.setLayout(self.main_layout)
        self.central_widget.layout.addWidget(self.content_widget, alignment=Qt.AlignCenter)

    def set_controller(self, controller):
        self.controller = controller

    def func_reset(self):
        self.ip_addr.setText("127.0.0.1")
        self.line_salle.clear()
        self.line_user.clear()
        self.checkbox_host.setChecked(False)

    def on_validate(self):
        if not self.line_user.text() or not self.line_salle.text():
            QMessageBox.warning(self, "Erreur", "Veuillez remplir tous les champs.")
            return

        # On émet le signal directement.
        # NOTE : Dans une vraie app, on attendrait la confirmation du serveur avant de changer de page.
        # Ici, le Controller dans main.py va tenter la connexion.
        self.switch_to_lobby.emit(
            self.line_salle.text(), 
            self.line_user.text(), 
            self.checkbox_host.isChecked()
        )