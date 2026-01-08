import sys
from PyQt5.QtWidgets import  QPushButton, QLineEdit, QTextEdit, QGridLayout, QVBoxLayout, QWidget, QToolBar, QMessageBox, QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QAction
from PyQt5.QtGui import QIcon, QKeySequence

    
class  calculefreq(QMainWindow):
    TITRE_FENETRE = " Calcule frequance "

    def __init__ (self):
        super().__init__ ()
        self.setWindowTitle(calculefreq.TITRE_FENETRE)
        self.resize(600,800)

        self.setStyleSheet("background-color : #254758;")


        #menu
        self.__menu_app = QMenu('&Application')

        self.__menu_aide = QMenu('&Aide')




        #reset
        self.__action_reset = QAction(QIcon('actions/gtk-new.png'), 'reset', self)
        self.__action_reset.setShortcut(QKeySequence.New)
        self.__action_reset.triggered.connect(self.fct_reset)

        self.__menu_app.addAction(self.__action_reset)



        #quitter
        self.__action_quitter = QAction(QIcon('actions/gtk-quit.png'), 'Quiter', self)
        self.__action_quitter.setShortcut(QKeySequence.Quit)
        self.__action_quitter.triggered.connect(self.fct_quitter)

        self.__menu_app.addAction(self.__action_quitter)


        self.menuBar().addMenu(self.__menu_app)


        #aide

        self.__action_aide = QAction(QIcon('actions/gtk-new.png'), 'A propos', self)
        self.__action_aide.triggered.connect(self.fct_aide)

        self.__menu_aide.addAction(self.__action_aide)
        self.menuBar().addMenu(self.__menu_aide)

        #toolbar

        self.__toolbar = QToolBar()
        self.__toolbar.addAction(self.__action_reset)
        self.__toolbar.addAction(self.__action_quitter)
        
        self.addToolBar(self.__toolbar)


        #Fenetre principale
        self.__blocprin = QWidget()
        self.__blocprin_lay = QVBoxLayout()
        self.__blocprin.setLayout(self.__blocprin_lay)
        
        
        self.setCentralWidget(self.__blocprin)
        #titre
        self.__titre = QLabel('frequance')
        self.__titre.setStyleSheet("color: white")
        self.__blocprin_lay.addWidget(self.__titre)


        #freq
        self.__bloc_sec  = QWidget()
        self.__bloc_sec_lay = QGridLayout()
        self.__bloc_sec.setLayout(self.__bloc_sec_lay)

        self.__f0 = QLabel('Fc0')
        self.__f1 = QLabel('Fc1')
        self.__f2 = QLabel('Fc2')





        self.__entree1 = QLineEdit()
        self.__entree1.setToolTip('freq1')
        self.__entree2 = QLineEdit()
        self.__entree2.setToolTip('freq2')
        self.__entree3 = QLineEdit()
        self.__entree3.setToolTip('freq3')



        self.__bloc_sec_lay.addWidget(self.__f0, 0,0)
        self.__bloc_sec_lay.addWidget(self.__f1, 1,0)
        self.__bloc_sec_lay.addWidget(self.__f2, 2,0)

        self.__bloc_sec_lay.addWidget(self.__entree1, 0,1)
        self.__bloc_sec_lay.addWidget(self.__entree2, 1,1)
        self.__bloc_sec_lay.addWidget(self.__entree3, 2,1)
        
        self.__blocprin_lay.addWidget(self.__bloc_sec)

        #titre2

        self.__titre2 = QLabel('calcule')
        self.__titre2.setStyleSheet("color: white")
        self.__blocprin_lay.addWidget(self.__titre2)

        #result

        self.__bloc_3  = QWidget()
        self.__bloc_3_lay = QGridLayout()
        self.__bloc_3.setLayout(self.__bloc_3_lay)

        self.__Resultat1 = QLabel('Resultat1')
        self.__Resultat2 = QLabel('Resultat2')

        self.__res1 = QLineEdit()
        self.__res2 = QLineEdit()
        self.__res1.setEnabled(False)
        self.__res2.setEnabled(False)
       

        self.__bloc_3_lay.addWidget(self.__Resultat1, 0,0)
        self.__bloc_3_lay.addWidget(self.__Resultat2, 1,0)

        self.__bloc_3_lay.addWidget(self.__res1, 0,1)
        self.__bloc_3_lay.addWidget(self.__res2, 1,1)

        self.__blocprin_lay.addWidget(self.__bloc_3)

        #bouton


        self.__bouton = QPushButton('Calcule')
        self.__blocprin_lay.addWidget(self.__bouton)
        self.__bouton.clicked.connect(self.calcule)




    def fct_quitter(self):
        sys.exit()

    def fct_reset(self):
        self.__entree1.setText('')
        self.__entree3.setText('')
        self.__entree2.setText('')
        self.__res1.setText('')
        self.__res2.setText('')

    def fct_aide(self):
        QMessageBox.information(self, "suiii", "suiiii")
        
    def calcule(self):
        fc0 = int(self.__entree1.text())
        fc1 = int(self.__entree2.text())
        fc2 = int(self.__entree3.text())

        resultat1 = fc0*fc1*fc2
        resultat2 = (fc0/fc1)/fc2

        self.__res1.setText(str(resultat1))
        self.__res2.setText(str(resultat2))

def main():
    application = QApplication(sys.argv)
    mon_appli = calculefreq()
    mon_appli.show()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()

