from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget
from PyQt5.QtCore import Qt

class RoomDialog(QDialog):
    def __init__(self, mode, parent=None):
        super().__init__(parent)
        self.mode = mode
        self.room_name = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Spot the RT - Join ou Host???")
        self.setFixedSize(350, 200)
        

        self.setStyleSheet("""
            QDialog {
                background-color: #1a333f; 
                border: 3px solid #00d4ff;
            }
            QLabel { 
                color: white; 
                font-weight: bold; 
                font-size: 12px;
                background-color: transparent;
            }
            QLineEdit { 
                border: 2px solid #00d4ff; 
                border-radius: 5px; 
                padding: 8px; 
                background-color: white; 
                color: black;
            }
            QPushButton { 
                background-color: #254758; 
                color: white; 
                border: 2px solid #00d4ff; 
                border-radius: 10px; 
                height: 40px; 
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00d4ff;
                color: #254758;
            }
        """)

        layout = QVBoxLayout(self)

        # Texte dynamique selon le mode
        txt = "NOM DE LA ROOM À CRÉER" if self.mode == "host" else "NOM DE LA ROOM À REJOINDRE"
        self.label = QLabel(txt)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.room_input = QLineEdit()
        self.room_input.setPlaceholderText("Ex: Dragon de l'enfer" \
        "Bouhahahaha")
        layout.addWidget(self.room_input)

        btn_txt = "CRÉER LA SALLE" if self.mode == "host" else "REJOINDRE LA SALLE"
        self.button = QPushButton(btn_txt)
        self.button.clicked.connect(self.validate)
        layout.addWidget(self.button)

    def validate(self):
        room = self.room_input.text().strip()
        if not room:
            QMessageBox.warning(self, "Erreur", "Le nom de la salle ne peut pas être vide.")
            return
        self.room_name = room
        self.accept()