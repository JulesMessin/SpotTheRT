from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from view.base_widgets import BackgroundWidget

class GamePage(QMainWindow):
    switch_to_results = pyqtSignal(str) # Signal avec nom du gagnant

    def __init__(self):
        super().__init__()
        self.controller = None
        self.setWindowTitle("Spot the RT - En jeu")
        self.resize(1100, 850)

        self.main_layout = QVBoxLayout()

        """ #----------------------------------------------------------------# """

        """ -- Header -- """
        self.header = QHBoxLayout()
        self.label_score = QLabel("Score : 0")
        self.label_score.setStyleSheet("font-size: 20px; color: white; font-weight: bold;")
        
        self.label_timer = QLabel("Temps : --")
        self.label_timer.setStyleSheet("font-size: 20px; color: #e74c3c; font-weight: bold;")
        
        self.btn_quit = QPushButton("Quitter")
        self.btn_quit.clicked.connect(self.close)

        self.header.addWidget(self.label_score)
        self.header.addStretch()
        self.header.addWidget(self.label_timer)
        self.header.addStretch()
        self.header.addWidget(self.btn_quit)
        self.main_layout.addLayout(self.header)

        """ #----------------------------------------------------------------# """

        """ -- Zone des Cartes -- """
        self.cards_layout = QHBoxLayout()
        
        # Carte Gauche
        self.card_left = QWidget()
        self.card_left.setFixedSize(400, 400)
        self.card_left.setStyleSheet("background-color: white; border-radius: 200px; border: 6px solid #2c3e50;")
        self.grid_left = QGridLayout(self.card_left)
        self.grid_left.setContentsMargins(50, 50, 50, 50)
        
        # Carte Droite
        self.card_right = QWidget()
        self.card_right.setFixedSize(400, 400)
        self.card_right.setStyleSheet("background-color: white; border-radius: 200px; border: 6px solid #2c3e50;")
        self.grid_right = QGridLayout(self.card_right)
        self.grid_right.setContentsMargins(50, 50, 50, 50)

        self.cards_layout.addStretch()
        self.cards_layout.addWidget(self.card_left)
        self.cards_layout.addSpacing(50)
        self.cards_layout.addWidget(self.card_right)
        self.cards_layout.addStretch()
        
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.cards_layout)
        self.main_layout.addStretch()

        """ #----------------------------------------------------------------# """

        # Bouton temporaire pour tester la fin du jeu
        self.btn_test = QPushButton("Simuler Victoire (Test)")
        self.btn_test.clicked.connect(lambda: self.switch_to_results.emit("Moi"))
        self.main_layout.addWidget(self.btn_test, alignment=Qt.AlignCenter)

        """ #----------------------------------------------------------------# """

        self.central_widget = BackgroundWidget("pp.jpg")
        self.setCentralWidget(self.central_widget)
        self.content_widget = QWidget()
        self.content_widget.setLayout(self.main_layout)
        self.central_widget.layout.addWidget(self.content_widget, alignment=Qt.AlignCenter)

    def set_controller(self, controller):
        self.controller = controller

    def update_cards_images(self, paths_left, paths_right):
        # Cette fonction sera appelée par le contrôleur quand le serveur envoie de nouvelles cartes
        # Nettoyer
        self.clear_grid(self.grid_left)
        self.clear_grid(self.grid_right)

        # Remplir (exemple simple)
        for i, path in enumerate(paths_left):
            self.add_image_to_grid(self.grid_left, path, i)
        for i, path in enumerate(paths_right):
            self.add_image_to_grid(self.grid_right, path, i)

    def clear_grid(self, grid):
        while grid.count():
            item = grid.takeAt(0)
            widget = item.widget()
            if widget: widget.deleteLater()

    def add_image_to_grid(self, grid, path, index):
        lbl = QLabel()
        pix = QPixmap(path).scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        lbl.setPixmap(pix)
        grid.addWidget(lbl, index // 3, index % 3)