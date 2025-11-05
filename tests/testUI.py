import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QMenuBar, QToolBar, QVBoxLayout, QWidget, QLabel, QLineEdit, QInputDialog, QMessageBox
from PyQt5.QtGui import QIcon

class InterfaceClientMail(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialiserUI()

    def initialiserUI(self):
        self.setWindowTitle('Client Mail')
        self.setGeometry(100, 100, 800, 600)
        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)
        disposition = QVBoxLayout(self.widget_central)

        self.champ_destinataire = QLineEdit(self)
        self.champ_destinataire.setPlaceholderText('Pour...')
        disposition.addWidget(self.champ_destinataire)

        self.champ_sujet = QLineEdit(self)
        self.champ_sujet.setPlaceholderText('Sujet...')
        disposition.addWidget(self.champ_sujet)

        self.zone_texte = QTextEdit(self)
        disposition.addWidget(self.zone_texte)

        self.creer_menus()
        self.creer_barre_outils()

    def creer_menus(self):
        barre_menu = self.menuBar()
        
        menu_fichier = barre_menu.addMenu('Fichier')

        action_nouveau = QAction(QIcon('/usr/share/icons/gnome/32x32/actions/mail-message-new.png'), 'Nouveau', self)
        menu_fichier.addAction(action_nouveau)
        
        action_envoyer = QAction(QIcon('/usr/share/icons/gnome/32x32/actions/mail-forward.png'), 'Envoyer', self)
        action_envoyer.triggered.connect(self.envoyer)
        menu_fichier.addAction(action_envoyer)
        
        action_effacer = QAction(QIcon('/usr/share/icons/gnome/32x32/actions/editclear.png'), 'Effacer', self)
        action_effacer.triggered.connect(self.effacer)
        menu_fichier.addAction(action_effacer)
        
        action_quitter = QAction(QIcon('/usr/share/icons/gnome/32x32/actions/system-log-out.png'), 'Quitter', self)
        action_quitter.triggered.connect(self.close)
        menu_fichier.addAction(action_quitter)
        
        menu_parametres = barre_menu.addMenu('Paramètres')
        action_serveur_smtp = QAction(QIcon('/usr/share/icons/gnome/32x32/actions/address-book-new.png'),'ServeurSMTP...', self)
        action_serveur_smtp.triggered.connect(self.definir_serveur_smtp)
        menu_parametres.addAction(action_serveur_smtp)
        
        action_expediteur = QAction(QIcon('/usr/share/icons/gnome/32x32/actions/mail-forward.png'),'Expéditeur...', self)
        action_expediteur.triggered.connect(self.definir_expediteur)
        menu_parametres.addAction(action_expediteur)
        
        action_signature = QAction(QIcon('/usr/share/icons/gnome/32x32/actions/format-text-direction-ltr.png'),'Signature...', self)
        action_signature.triggered.connect(self.definir_signature)
        menu_parametres.addAction(action_signature)
        menu_aide = barre_menu.addMenu('Aide')
        
        action_a_propos = QAction(QIcon('/usr/share/icons/gnome/32x32/actions/help-faq.png'),'A propos', self)
        action_a_propos.triggered.connect(self.afficher_a_propos)
        menu_aide.addAction(action_a_propos)

    def creer_barre_outils(self):
        barre_outils = QToolBar('Outils')
        action_envoyer = QAction(QIcon('/usr/share/icons/gnome/32x32/actions/mail-send.png'), 'Envoyer', self)
        action_envoyer.triggered.connect(self.envoyer)
        action_effacer = QAction(QIcon('/usr/share/icons/gnome/32x32/actions/editclear.png'), 'Effacer', self)
        action_effacer.triggered.connect(self.effacer)
        barre_outils.addAction(action_envoyer)
        barre_outils.addAction(action_effacer)
        self.addToolBar(barre_outils)

    def envoyer(self):
        destinataire = self.champ_destinataire.text()
        sujet = self.champ_sujet.text()
        contenu = self.zone_texte.toPlainText()
        print(f"Destinataire: {destinataire}")
        print(f"Sujet: {sujet}")
        print(f"Contenu: {contenu}")

    def effacer(self):
        self.champ_destinataire.clear()
        self.champ_sujet.clear()
        self.zone_texte.clear()

    def definir_serveur(self):
        serveur_smtp = QInputDialog.getText(self, 'Serveur SMTP', 'Entrez l\'adresse du serveur SMTP:')
        if serveur_smtp:
            print(f"Serveur SMTP défini: {serveur_smtp}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = InterfaceClientMail()
    fenetre.show()
    sys.exit(app.exec_())

