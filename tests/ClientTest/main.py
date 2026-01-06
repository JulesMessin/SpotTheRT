import sys
from PyQt5.QtWidgets import QApplication
from page_connexion import SpotTheRT

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = SpotTheRT()
    fenetre.show()
    sys.exit(app.exec_())