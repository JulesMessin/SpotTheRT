from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class RoomDialog(QDialog):
    def __init__(self, mode, parent=None):
        super().__init__(parent)
        self.mode = mode
        self.room_name = None
        self.setWindowTitle("Nom de la room")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout(self)

        label_text = "Nom de la room à créer" if mode == "host" else "Nom de la room à rejoindre"
        self.label = QLabel(label_text)
        layout.addWidget(self.label)

        self.room_input = QLineEdit()
        layout.addWidget(self.room_input)

        button_text = "Créer la room" if mode == "host" else "Se connecter"
        self.button = QPushButton(button_text)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.validate)

    def validate(self):
        room = self.room_input.text().strip()
        if not room:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un nom de room")
            return
        self.room_name = room
        self.accept() 
