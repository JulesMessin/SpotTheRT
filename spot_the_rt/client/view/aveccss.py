import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QPushButton, QWidget, QLineEdit, QLabel, QCheckBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap


class BackgroundWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image = QPixmap(image_path)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # pas d'espace autour

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)  # dessine le fond sur tout le widget








class Spot_the_rt(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spot the rt")
        self.resize(700, 800)


        """ # --- Layout principal vertical ---"""
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.main_layout.setSpacing(100)

        """#----------------------------------------------------------------#"""
#----------------------------------------------------------------#



        """ -- Top layout -- """
        self.top_layout = QHBoxLayout()
        
        """ - bouton reset - """
        self.button_reset = QPushButton("Reset")
        self.button_reset.clicked.connect(self.func_reset)
        
        """ - bouton fermer - """
        self.button_fermer = QPushButton("Fermer")
        self.button_fermer.clicked.connect(self.close)
        
        """ - oranisation du layer - """
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.button_reset)  
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.button_fermer)
        self.top_layout.addStretch()
        
        """ - ajout top layout au main layout - """
        self.main_layout.addLayout(self.top_layout)



#----------------------------------------------------------------#



        """ -- Ip layout -- """
        self.ip_layout = QHBoxLayout()
        
        """ - creation label - """
        self.label_ip_server = QLabel("Adresse IP du serveur :")
        
        """ - creation qlineedit - """
        self.ip_addr = QLineEdit()
        self.ip_addr.setAlignment(Qt.AlignCenter)
        
        """ - oranisation du layer - """ 
        self.ip_layout.addStretch()
        self.ip_layout.addWidget(self.label_ip_server)
        self.ip_layout.addWidget(self.ip_addr)
        self.ip_layout.addStretch()
        """ - ajout ip layout au main layout - """
        self.main_layout.addLayout(self.ip_layout)



#----------------------------------------------------------------#



        """ -- Salle layout -- """        
        self.salle_layout = QHBoxLayout()
        
        """ - creation label - """
        self.label_salle = QLabel("Nom de la salle :")
        
        """ - creation qlineedit - """
        self.line_salle = QLineEdit()
        self.line_salle.setAlignment(Qt.AlignCenter)
        
        """ - oranisation du layer - """ 
        self.salle_layout.addStretch()
        self.salle_layout.addWidget(self.label_salle)
        self.salle_layout.addWidget(self.line_salle)
        self.salle_layout.addStretch()
        """ - ajout salle layout au main layout - """
        self.main_layout.addLayout(self.salle_layout)



#----------------------------------------------------------------#



        """ -- Host layout -- """
        self.host_layout = QHBoxLayout()
        
        """ - creation checkbox - """
        self.checkbox_host = QCheckBox("Hôte")
        
        """ - oranisation du layer - """ 
        self.host_layout.addStretch()
        self.host_layout.addWidget(self.checkbox_host)
        self.host_layout.addStretch()
        
        """ - ajout host layout au main layout - """
        self.main_layout.addLayout(self.host_layout)

        
        
#----------------------------------------------------------------#


        
        """ -- User layout -- """
        self.user_layout = QHBoxLayout()
        
        """ - creation label - """
        self.label_user = QLabel("Nom d’utilisateur :")
        
        """ - creation qlineedit - """
        self.line_user = QLineEdit()
        self.line_user.setAlignment(Qt.AlignCenter)
        """ - oranisation du layer - """ 
        self.user_layout.addStretch()
        self.user_layout.addWidget(self.label_user)
        self.user_layout.addWidget(self.line_user)
        self.user_layout.addStretch()
        
        """ - ajout user layout au main layout - """
        self.main_layout.addLayout(self.user_layout)
        


#----------------------------------------------------------------#



        """ -- Bottom layout -- """       
        self.bottomlayout = QHBoxLayout()
        
        """ - bouton fermer - """
        self.button_valider = QPushButton("Valider")
        self.button_fermer.clicked.connect(self.Valider)
        
        """ - oranisation du layer - """ 
        self.bottomlayout.addStretch()
        self.bottomlayout.addWidget(self.button_valider)
        self.bottomlayout.addStretch()
        
        """ - ajout bottom layout au main layout - """
        self.main_layout.addLayout(self.bottomlayout)
        
        
        
#----------------------------------------------------------------#
        """#----------------------------------------------------------------#"""
        
        
         
        """ # --- Définir le widget central --- """
        #self.central_widget = QWidget()
        self.central_widget = BackgroundWidget("pp.jpg")
        """
        #self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        self.main_layout.addStretch()
        self.central_widget.layout.addLayout(self.main_layout)
        """
        self.setCentralWidget(self.central_widget)

# Crée un widget qui contient ton layout principal
        self.content_widget = QWidget()
        self.content_widget.setLayout(self.main_layout)

# Option 1 : pour centrer verticalement et horizontalement
        self.central_widget.layout.addStretch()
        self.central_widget.layout.addWidget(self.content_widget, alignment=Qt.AlignCenter)
        self.central_widget.layout.addStretch()




        
    def func_reset(self):
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
