from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QLineEdit, QPushButton
)

class GameView(QMainWindow):
    def __init__(self, username, room_name):
        super().__init__()
        self.username = username
        self.room_name = room_name
        self.controller = None

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(f"Jeu - {self.room_name}")
        self.setGeometry(200, 200, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.info_label = QLabel(f"{self.username} dans la room '{self.room_name}'")
        layout.addWidget(self.info_label)

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        layout.addWidget(self.chat_area)

        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Entrez votre message ici...")
        layout.addWidget(self.message_input)

        self.send_button = QPushButton("Envoyer le message")
        layout.addWidget(self.send_button)

        self.quit_button = QPushButton("Quitter la partie")
        layout.addWidget(self.quit_button)

    def set_controller(self, controller):
        self.controller = controller

        self.send_button.clicked.connect(self.on_send)

        self.quit_button.clicked.connect(lambda: self.controller.leave_game(self.room_name))

    def on_send(self):
        message = self.message_input.toPlainText().strip()
        if message and self.controller:
            self.controller.send_message(message)
            self.message_input.clear()

    def display_message(self, message):
        self.chat_area.append(message)
