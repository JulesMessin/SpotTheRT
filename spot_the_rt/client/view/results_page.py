from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt, pyqtSignal
from view.base_widgets import BackgroundWidget

class ResultsPage(QMainWindow):
    switch_to_menu = pyqtSignal()

    def __init__(self, winner_name):
        super().__init__()
        self.setWindowTitle("Résultats")
        self.resize(700, 800)

        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(40)

        """ #----------------------------------------------------------------# """

        self.label_title = QLabel("FIN DE PARTIE")
        self.label_title.setStyleSheet("font-size: 40px; color: gold; font-weight: bold;")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.label_title)

        self.label_winner = QLabel(f"Gagnant : {winner_name}")
        self.label_winner.setStyleSheet("font-size: 28px; color: white; background-color: rgba(0,0,0,150); padding: 10px; border-radius: 10px;")
        self.label_winner.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.label_winner)

        """ #----------------------------------------------------------------# """

        self.btn_replay = QPushButton("Retour Menu")
        self.btn_replay.clicked.connect(lambda: self.switch_to_menu.emit())
        self.main_layout.addWidget(self.btn_replay)
        
        self.btn_quit = QPushButton("Quitter")
        self.btn_quit.setStyleSheet("background-color: #c0392b; color: white;")
        self.btn_quit.clicked.connect(self.close)
        self.main_layout.addWidget(self.btn_quit)

        """ #----------------------------------------------------------------# """

        self.central_widget = BackgroundWidget("pp.jpg")
        self.setCentralWidget(self.central_widget)
        self.content_widget = QWidget()
        self.content_widget.setLayout(self.main_layout)
        self.central_widget.layout.addWidget(self.content_widget, alignment=Qt.AlignCenter)